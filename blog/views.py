from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Blog


class BlogListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "blog.html"
    context_object_name = "blog"
    ordering = [
        "-is_published",
        "-created_at",
    ]

    def get_queryset(self):
        """Переопределяет метод get_queryset - показывает только опубликованные статьи"""
        user = self.request.user
        if user.is_superuser or user.has_perm("blog.change_blog"):
            queryset = Blog.objects.all()
        else:
            queryset = Blog.objects.filter(is_published=True)
        return queryset.order_by("-is_published", "-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["published_count"] = Blog.objects.filter(is_published=True).count()
        context["unpublished_count"] = Blog.objects.filter(is_published=False).count()
        return context


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """Класс CBV для отображения одной статьи подробно. Только для авторизованных пользователей"""

    model = Blog
    template_name = "article_details.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        """Переопределяет метод get_object, добавляя вс него увеличение счетчика просмотров при открытии статьи"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс CBV для создания новой статьи по форме"""

    model = Blog
    fields = ["title", "content", "is_published", "preview"]
    template_name = "article_form.html"
    permission_required = "blog.add_blog"

    def get_success_url(self):
        return reverse_lazy("blog:blog")


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс CBV для редактирования существующей статьи в форме"""

    model = Blog
    fields = ["title", "content", "is_published", "preview"]
    template_name = "article_form.html"
    permission_required = "blog.change_blog"

    def get_success_url(self):
        """После редактирования статьи - возвращает на страницу с этой статьей"""
        return reverse("blog:article_details", args=[self.kwargs.get("pk")])


class ArticleDeliteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс CBV для удаления статьи"""

    model = Blog
    template_name = "blog_confirm_delete.html"
    permission_required = "blog.delete_blog"

    def get_success_url(self):
        return reverse_lazy("blog:articles")
