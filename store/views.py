from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    # Дістаємо з бази всі доступні товари та всі категорії
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    # Передаємо їх у шаблон
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories
    })