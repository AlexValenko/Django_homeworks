from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    ArticleCreateView,
    ArticleDeliteView,
    ArticleDetailView,
    ArticleUpdateView,
    BlogArticlesListView,
    BlogListView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("editor/", ArticleCreateView.as_view(), name="article_create"),
    path("editor/<int:pk>", ArticleUpdateView.as_view(), name="article_edit"),
    path("editor/<int:pk>/delete/", ArticleDeliteView.as_view(), name="article_delete"),
    path("articles/", BlogArticlesListView.as_view(), name="articles"),
    path("blog/", BlogListView.as_view(), name="blog"),
    # path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("article_details/<int:pk>", ArticleDetailView.as_view(), name="article_details"),
]
