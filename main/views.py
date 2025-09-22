import logging
import datetime

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
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    data = FootballItem.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

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
    form = UserCreationForm()

    if request.method == "POST": # Why post? because we want to send sensitive data to the server
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('main:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.delete_cookie('last_login')
    return response