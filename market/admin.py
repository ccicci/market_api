from django.contrib import admin
from market.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_display_links = ['title']
    list_per_page = 10
    list_filter = ['category', 'status']