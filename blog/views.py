from django.views.generic import ListView, DetailView

from .models import Blog


class BlogListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "blog.html"
    context_object_name = 'blog'

    # def get_queryset(self):
    #     return Blog.objects.filter(is_published=True)

class BlogArticlesListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "articles.html"
    context_object_name = 'blog'

    # def get_queryset(self):
    #     return Blog.objects.filter(is_published=True)

class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'article_details.html'
    context_object_name = 'article'
