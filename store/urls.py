from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Головна сторінка магазину
    path('', views.product_list, name='product_list'),
]