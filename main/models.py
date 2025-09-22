from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FootballItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, help_text="Name of the football item")
    price = models.IntegerField(help_text="Price in rupiah")
    description = models.TextField(help_text="Detailed description of the item")
    thumbnail = models.URLField(max_length=500, help_text="URL to item image")
    category = models.CharField(max_length=100, help_text="Item category (e.g., Jersey, Boots, Ball)")
    is_featured = models.BooleanField(default=False, help_text="Whether this item is featured")
    # Additional
    brand = models.CharField(max_length=100, blank=True, null=True, help_text="Brand name (e.g., Nike, Adidas)")
    stock = models.IntegerField(default=0, help_text="Number of items in stock")
    size = models.CharField(max_length=10, blank=True, null=True, help_text="Size (S, M, L, XL, or shoe sizes)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)