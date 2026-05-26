from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Категорія")
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    
    has_anc = models.BooleanField(default=False, verbose_name="Активне шумозаглушення (ANC)")
    supports_custom_eq = models.BooleanField(default=False, verbose_name="Кастомний 9-смуговий еквалайзер")
    
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Зображення")
    available = models.BooleanField(default=True, verbose_name="В наявності")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.name