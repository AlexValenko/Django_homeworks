from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Blog


class BlogListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "blog.html"
    context_object_name = "blog"

    def get_queryset(self):
        """Переопределяет метод get_queryset - показывает только опубликованные статьи"""
        return Blog.objects.filter(is_published=True)


class BlogArticlesListView(ListView):
    """Класс CBV для отображения страницы "Статьи"- карточки со статьями блога"""

    model = Blog
    template_name = "articles.html"
    context_object_name = "blog"

    def get_queryset(self):
        """Переопределяет метод get_queryset - показывает только опубликованные статьи"""
        return Blog.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    """Класс CBV для отображения одной статьи подробно"""

    model = Blog
    template_name = "article_details.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        """Переопределяет метод get_object, добавляя вс него увеличение счетчика просмотров при открытии статьи"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    """Класс CBV для создания новой статьи по форме"""

    model = Blog
    fields = ["title", "content", "is_published", "preview"]
    template_name = "article_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:articles")


class ArticleUpdateView(UpdateView):
    """Класс CBV для редактирования существующей статьи в форме"""

    model = Blog
    fields = ["title", "content", "is_published", "preview"]
    template_name = "article_form.html"

    def get_success_url(self):
        """После редактирования статьи - возвращает на страницу с этой статьей"""
        return reverse("blog:article_details", args=[self.kwargs.get("pk")])


class ArticleDeliteView(DeleteView):
    """Класс CBV для удаления статьи"""

    model = Blog
    template_name = "blog_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("blog:articles")
