from django.shortcuts import render
from .models import Product, Category, Feature

def product_list(request):
    # Дістаємо з бази всі доступні товари та всі категорії
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    features = Feature.objects.all()

    category_slug = request.GET.get('category')
    feature_slug = request.GET.get('feature')

    if category_slug:
        products = products.filter(category__slug=category_slug)
    if feature_slug:
        products = products.filter(features__slug=feature_slug)
    
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'features': features,
        'current_category': category_slug,
        'current_feature': feature_slug,
    })