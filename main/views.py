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

@login_required(login_url='/login')
def show_json(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        footballitems_list = FootballItem.objects.all()
    else:
        footballitems_list = FootballItem.objects.filter(user=request.user)
    
    data = [{
        'id': item.id,
        'name': item.name,
        'price': item.price,
        'description': item.description,
        'thumbnail': item.thumbnail,
        'category': item.category,
        'brand': item.brand,
        'stock': item.stock,
        'size': item.size,
        'created_at': item.created_at.isoformat() if item.created_at else None,
        'is_featured': item.is_featured,
        'user': {
            'id': item.user.id if item.user else None,
            'username': item.user.username if item.user else 'Unknown'
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

def register(request):
    if request.method == "POST":
        # Check if this is an AJAX request
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            if is_ajax:
                return JsonResponse({
                    'status': 'success',
                    'message': 'Account successfully created! Please login.',
                    'redirect': reverse('main:login')
                }, status=201)
            else:
                messages.success(request, 'Account successfully created!')
                return redirect('main:login')
        else:
            if is_ajax:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(error) for error in error_list]
                return JsonResponse({
                    'status': 'error',
                    'message': 'Registration failed. Please check your inputs.',
                    'errors': errors
                }, status=400)
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        # Check if this is an AJAX request
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if is_ajax:
                return JsonResponse({
                    'status': 'success',
                    'message': 'Login successful!',
                    'redirect': reverse('main:show_main'),
                    'username': user.username
                }, status=200)
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            if is_ajax:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(error) for error in error_list]
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid username or password.',
                    'errors': errors
                }, status=400)
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
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
@login_required(login_url='/login')
def create_football_item_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    size = request.POST.get("size")
    is_featured = request.POST.get("is_featured") == 'on'
    
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
        user=request.user
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