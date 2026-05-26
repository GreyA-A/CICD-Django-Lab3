from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'has_anc', 'supports_custom_eq', 'available']
    list_filter = ['available', 'has_anc', 'supports_custom_eq', 'category']
    list_editable = ['price', 'available']