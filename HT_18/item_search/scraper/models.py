from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=50, unique=True, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Назва')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    short_description = models.TextField(blank=True, null=True, verbose_name='Короткий опис')
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='Бренд')
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='Категорія')
    link_to_product = models.URLField(max_length=255, verbose_name='Лінк на продукт')
    update_date = models.DateTimeField(verbose_name='Дата оновлення даних')

    def __str__(self):
        return self.name

