from django.core.cache import cache

from .models import Category


def categories(request):
    """Функция добавляет в шаблон переменную categories со списком категорий товаров.
    Значение берется из кэша и хранится 15 минут"""
    cached_categories = cache.get("cached_categories")
    if cached_categories is None:
        cached_categories = {"categories": Category.objects.all()}
        cache.set("cached_categories", cached_categories, 60 * 15)
    return cached_categories
