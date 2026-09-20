from django.views.generic import ListView

from .models import Blog


class BlogListView(ListView):
    """Класс CBV для отображения домашней страницы - карточки со статьями блога"""

    model = Blog
    template_name = "blog.html"
