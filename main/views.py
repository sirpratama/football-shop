import logging
import datetime
import json

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import FootballItemForm
from main.models import FootballItem
from django.core import serializers
from django.http import HttpResponse
from django.core.management import call_command
from django.db import connection
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        football_items = FootballItem.objects.all()
    else:
        football_items = FootballItem.objects.filter(user=request.user)

    context = {
        'npm' : '2406453556',
        'name': request.user.username,
        'class': 'KKI',
        'football_items': football_items,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_football_item(request):
    form = FootballItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        football_item_entry = form.save(commit=False)
        football_item_entry.user = request.user
        football_item_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_football_item.html", context)

@login_required(login_url='/login')
def show_football_item_detail(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)

    context = {
        'football_item': football_item,
    }

    return render(request, "show_football_item_detail.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = FootballItem.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get("filter", "all")
    user_id = request.GET.get("user_id")  # Workaround for cookie issues
    
    if filter_type == "all":
        footballitems_list = FootballItem.objects.all()
    else:
        # Try to get user from session or from user_id parameter
        if request.user.is_authenticated:
            footballitems_list = FootballItem.objects.filter(user=request.user)
        elif user_id:
            # Fallback: use provided user_id
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(id=user_id)
                footballitems_list = FootballItem.objects.filter(user=user)
            except User.DoesNotExist:
                return JsonResponse([], safe=False, status=401)
        else:
            return JsonResponse([], safe=False, status=401)
    
    # Format data to match Flutter's Product model structure
    data = [{
        'model': 'main.footballitem',
        'pk': str(item.id),
        'fields': {
            'user': item.user.id if item.user else None,
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'category': item.category,
            'is_featured': item.is_featured,
        }
    }
    for item in footballitems_list
    ]
    return JsonResponse(data, safe=False)

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    try:
        data = FootballItem.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except FootballItem.DoesNotExist:
        return HttpResponse(status=404)

@login_required(login_url='/login')
def show_json_by_id(request, id):
    try:
        data = FootballItem.objects.filter(pk=id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    except FootballItem.DoesNotExist:
        return HttpResponse(status=404)

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # Always return JSON for POST requests (used by Flutter)
            return JsonResponse({
                'status': 'success',
                'message': 'Account successfully created! Please login.',
                'username': user.username
            }, status=201)
        else:
            # Return JSON with errors
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': 'error',
                'message': 'Registration failed. Please check your inputs.',
                'errors': errors
            }, status=400)
    else:
        # GET request - show HTML form
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Always return JSON for POST requests (used by Flutter)
            return JsonResponse({
                'status': True,
                'message': 'Login successful!',
                'username': user.username,
                'user_id': user.id  # Add user_id for Flutter workaround
            }, status=200)
        else:
            # Return JSON with errors
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': False,
                'message': 'Invalid username or password.',
                'errors': errors
            }, status=401)
    else:
        # GET request - show HTML form
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    logout(request)
    
    # Check if this is an API request (from Flutter)
    is_api = request.content_type == 'application/x-www-form-urlencoded' or request.method == 'POST'
    
    if is_api and request.method == 'POST':
        return JsonResponse({
            'status': True,
            'message': 'Logged out successfully!',
            'username': username
        }, status=200)
    else:
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response

def edit_football_item(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)
    form = FootballItemForm(request.POST or None, instance=football_item)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}

    return render(request, 'edit_football_item.html', context)

def delete_football_item(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)
    football_item.delete()
    return redirect('main:show_main')

@csrf_exempt
@require_POST
def create_football_item_ajax(request):
    # Debug logging
    print(f"User authenticated: {request.user.is_authenticated}")
    print(f"User: {request.user}")
    print(f"Session key: {request.session.session_key}")
    print(f"Cookies: {request.COOKIES}")
    
    # TEMPORARY WORKAROUND: Get user ID from POST data instead of session
    # This is a workaround for Flutter Web cookie issues
    user_id = request.POST.get('user_id')
    
    # Check if user is authenticated OR if user_id is provided
    if not request.user.is_authenticated and not user_id:
        return JsonResponse({
            'status': 'error',
            'message': 'You must be logged in to create products.'
        }, status=401)
    
    # Get the actual user
    if request.user.is_authenticated:
        user = request.user
    else:
        # Fallback: use provided user_id
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid user.'
            }, status=401)
    
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    size = request.POST.get("size")
    # Handle boolean from Flutter or 'on' from web form
    is_featured_value = request.POST.get("is_featured")
    is_featured = is_featured_value in ['true', 'True', 'on', True]
    
    new_item = FootballItem(
        name=name,
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        brand=brand if brand else None,
        stock=stock if stock else 0,
        size=size if size else None,
        is_featured=is_featured,
        user=user  # Use the user we determined above
    )
    new_item.save()
    
    return JsonResponse({
        'status': 'success',
        'message': 'Football item created successfully!',
        'item': {
            'id': new_item.id,
            'name': new_item.name,
            'price': new_item.price,
            'category': new_item.category,
        }
    }, status=201)

@login_required(login_url='/login')
def edit_football_item_ajax(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)
    
    # Check if user owns this item
    if football_item.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    if request.method == 'POST':
        form = FootballItemForm(request.POST, instance=football_item)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Football item updated successfully!',
                'item': {
                    'id': football_item.id,
                    'name': football_item.name,
                    'price': football_item.price,
                    'category': football_item.category,
                }
            }, status=200)
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid form data',
                'errors': form.errors
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required(login_url='/login')
def delete_football_item_ajax(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)
    
    # Check if user owns this item
    if football_item.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    if request.method == 'DELETE':
        football_item.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Football item deleted successfully!'
        }, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)