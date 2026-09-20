from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsFormView, ProductDetailView, ProductCreateView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("add_product/", ProductCreateView.as_view(), name="add_product"),
    path("products/", ProductListView.as_view(), name="products"),
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("product_details/<int:pk>", ProductDetailView.as_view(), name="product_details"),
]
