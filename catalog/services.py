from .models import Product
from django.core.cache import cache


def get_products_by_category(category_id):
    """Принимает идентификатор категории товаров. Хранит в кэше 15 минут все товары.
    Возвращает список товаров указанной категории. Создает ключ кэша на каждую категорию товаров """

    cache_key = f"products_category_{category_id}"
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id).order_by("prod_name"))
        cache.set(cache_key, products, 60*15)

    return products


def get_products_list():
    """Возвращает общий список товаров из кеша на 15 минут."""

    products_list = cache.get("products_list")

    if products_list is None:
        products_list = list(Product.objects.order_by("category__category_name"))
        cache.set("products_list", products_list, 60 * 15)

    return products_list
