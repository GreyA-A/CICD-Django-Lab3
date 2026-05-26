import pytest
from django.urls import reverse
from store.models import Category, Product

@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(name="Студійні монітори", slug="studio-monitors")
    assert category.name == "Студійні монітори"
    assert str(category) == "Студійні монітори"

@pytest.mark.django_db
def test_product_creation():
    category = Category.objects.create(name="Навушники", slug="headphones")
    product = Product.objects.create(
        category=category,
        name="Sony WH-CH720N",
        price=3500.00,
        has_anc=True,
        supports_custom_eq=True
    )
    assert product.price == 3500.00
    assert product.has_anc is True

@pytest.mark.django_db
def test_product_list_view(client):
    # Спочатку створюємо тестові дані
    category = Category.objects.create(name="TWS", slug="tws")
    Product.objects.create(
        category=category,
        name="Test Audio Pro",
        price=1000.00
    )
    
    # Робимо HTTP GET-запит до головної сторінки магазину
    url = reverse('store:product_list')
    response = client.get(url)
    
    # Перевіряємо, чи сервер віддав успішний статус 200 (OK)
    assert response.status_code == 200
    # Перевіряємо, чи назва нашого товару дійсно з'явилася в HTML-коді
    assert b"Test Audio Pro" in response.content