from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import add_product, contacts, product_details, products, HomeListView

app_name = CatalogConfig.name

urlpatterns = [
    # path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_details/<int:pk>", product_details, name="product_details"),
    path("add_product/", add_product, name="add_product"),
    path("products/", products, name="products"),
    path("home/", HomeListView.as_view(), name="home"),
]
