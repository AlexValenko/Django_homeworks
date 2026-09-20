from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Blog


class BlogListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "blog.html"
    context_object_name = "blog"

    # def get_queryset(self):
    #     return Blog.objects.filter(is_published=True)


class BlogArticlesListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "articles.html"
    context_object_name = "blog"

    # def get_queryset(self):
    #     return Blog.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Blog
    template_name = "article_details.html"
    context_object_name = "article"


class ArticleCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "is_published", "preview"]
    template_name = "article_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:articles")


class ArticleUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "is_published", "preview"]
    template_name = "article_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:articles")


class ArticleDeliteView(DeleteView):
    model = Blog
    template_name = "blog_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("blog:articles")
