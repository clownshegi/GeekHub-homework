from django.shortcuts import get_object_or_404, redirect, render
from subprocess import Popen

from .models import ScrapingTask, Product


def index(request):
    return render(request, 'index.html', {'title': 'Main'})


def add_product(request):
    return render(request, 'add_product.html', {'title': 'Add product'})


def product_data(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})


def scraper_data(request):
    response = request.GET.get('id_string')
    ScrapingTask.objects.create(input_string=response)
    Popen(['python3', 'subscraper.py'])
    return redirect('scraper:add_product')


def show_my_products(request):
    return render(request, 'show_my_products.html', {'products': Product.objects.all()})

