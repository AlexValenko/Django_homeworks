from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogArticlesListView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    # path("add_product/", ProductCreateView.as_view(), name="add_product"),
    path("articles/", BlogArticlesListView.as_view(), name="articles"),
    path("blog/", BlogListView.as_view(), name="blog"),
    # path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("article_details/<int:pk>", ArticleDetailView.as_view(), name="article_details"),
]
