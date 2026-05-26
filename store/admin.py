from django.contrib import admin
from .models import Category, Feature, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'available']
    list_filter = ['available', 'category', 'features']
    list_editable = ['price', 'available']
    filter_horizontal = ['features']