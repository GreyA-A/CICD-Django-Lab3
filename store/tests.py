import pytest
from django.urls import reverse
from store.models import Category, Product, Feature

@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(name="Студійні монітори", slug="studio-monitors")
    assert category.name == "Студійні монітори"

@pytest.mark.django_db
def test_product_creation():
    category = Category.objects.create(name="Навушники", slug="headphones")
    feature_anc = Feature.objects.create(name="ANC", slug="anc")
    
    product = Product.objects.create(
        category=category,
        name="Sony WH-CH720N",
        price=3500.00
    )
    product.features.add(feature_anc)
    
    assert product.price == 3500.00
    assert feature_anc in product.features.all()

@pytest.mark.django_db
def test_product_list_view(client):
    category = Category.objects.create(name="TWS", slug="tws")
    Product.objects.create(category=category, name="Test Audio Pro", price=1000.00)
    
    url = reverse('store:product_list')
    response = client.get(url)
    
    assert response.status_code == 200
    assert b"Test Audio Pro" in response.content