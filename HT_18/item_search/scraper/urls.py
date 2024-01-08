from django.urls import path

from . import views

app_name = "scraper"
urlpatterns = [
    path("", views.product_input, name="product_input"),
    path("products", views.ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product_details"),
]