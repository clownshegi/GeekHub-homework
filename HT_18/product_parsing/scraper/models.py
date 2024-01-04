from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=15)
    brand_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255,)
    discounted_price = models.CharField(max_length=10)
    product_link = models.CharField(max_length=255)


class ScrapingTask(models.Model):
    input_string = models.CharField(max_length=1000)
