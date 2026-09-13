from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_details/<int:pk>", product_details, name="product_details"),
]
