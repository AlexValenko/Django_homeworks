from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView

app_name = BlogConfig.name

urlpatterns = [
    # path("add_product/", ProductCreateView.as_view(), name="add_product"),
    # path("products/", ProductListView.as_view(), name="products"),
    path("blog/", BlogListView.as_view(), name="blog"),
    # path("contacts/", ContactsFormView.as_view(), name="contacts"),
    # path("product_details/<int:pk>", ProductDetailView.as_view(), name="product_details"),
]
