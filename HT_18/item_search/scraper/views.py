from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .forms import GetProductIdsForm
from .models import Product
from .services import handle_valid_data


def product_input(request):
    success_message = None

    if request.method == 'POST':
        form = GetProductIdsForm(request.POST)
        if form.is_valid():
            handle_valid_data(form.cleaned_data)
            success_message = 'Дані успішно додані в чергу на обробку!'
        else:
            success_message = "Дозволені тільки латинські букви, цифри та кома!"

    form = GetProductIdsForm()
    return render(request, 'product_input.html', {'form': form, 'success_message': success_message})


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products_list"
    paginate_by = 10
    ordering = ['-update_date']


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product_details"