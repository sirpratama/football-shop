from django.shortcuts import render, redirect, get_object_or_404
from main.forms import FootballItemForm
from main.models import FootballItem
from django.core import serializers
from django.http import HttpResponse
from django.core.management import call_command
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def show_main(request):
    # Check if the table exists and run migrations if needed
    try:
        football_items = FootballItem.objects.all()
    except Exception as e:
        # If table doesn't exist, run migrations
        if "does not exist" in str(e) or "no such table" in str(e):
            try:
                logger.info("Running database migrations...")
                call_command('migrate', verbosity=0, interactive=False)
                football_items = FootballItem.objects.all()
            except Exception as migration_error:
                logger.error(f"Migration failed: {migration_error}")
                # Return an error page or create an empty queryset
                football_items = FootballItem.objects.none()
        else:
            raise e
    
    # Create sample data if database is empty (for PWS deployment)
    if not football_items.exists():
        sample_items = [
            {
                'name': 'Manchester United Home Jersey',
                'price': 750000,
                'description': 'Official Manchester United home jersey for the 2024/25 season. Made with high-quality materials and featuring the classic red color with white accents.',
                'thumbnail': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
                'category': 'Jersey',
                'brand': 'Adidas',
                'is_featured': True,
                'stock': 25,
                'size': 'L'
            },
            {
                'name': 'Nike Premier League Football',
                'price': 450000,
                'description': 'Official Nike Premier League match ball. FIFA Quality Pro certified with innovative design for superior flight and touch.',
                'thumbnail': 'https://images.unsplash.com/photo-1486286701208-1d58e9338013?w=400',
                'category': 'Ball',
                'brand': 'Nike',
                'is_featured': False,
                'stock': 15,
                'size': '5'
            },
            {
                'name': 'Adidas Predator Football Boots',
                'price': 1200000,
                'description': 'Professional football boots with innovative Predator technology. Designed for precision, power, and control on the pitch.',
                'thumbnail': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=400',
                'category': 'Boots',
                'brand': 'Adidas',
                'is_featured': True,
                'stock': 8,
                'size': '42'
            }
        ]
        
        for item_data in sample_items:
            FootballItem.objects.create(**item_data)
        
        # Refresh the queryset after creating sample data
        football_items = FootballItem.objects.all()

    context = {
        'npm' : '2406453556',
        'name': 'Muhammad Rafi Nazir Pratama',
        'class': 'KKI',
        'football_items': football_items,
    }

    return render(request, "main.html", context)

def create_football_item(request):
    form = FootballItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_football_item.html", context)

def show_football_item_detail(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)

    context = {
        'football_item': football_item,
    }

    return render(request, "show_football_item_detail.html", context)

def show_xml(request):
    data = FootballItem.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    data = FootballItem.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        data = FootballItem.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except FootballItem.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        data = FootballItem.objects.filter(pk=id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    except FootballItem.DoesNotExist:
        return HttpResponse(status=404)