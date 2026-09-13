from itertools import product

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    """Контроллер для отображения домашней страницы - отображает последние 6 добавленных товаров"""

    latest_products = Product.objects.order_by('created_at')[:6]
    context = {"products" : latest_products}

    if latest_products:
        return render(request, "home.html", context=context)


def contacts(request):
    """Метод для отправки страницы Контакты, и получения формы обратной связи"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'Получена обратная связь от {name} ({phone}). Текст сообщения "{message}"')
        return HttpResponse(f"Спасибо, {name}! сообщение получено.")
    return render(request, "contacts.html")

def product_details(request, pk):
    """Контроллер для отображения подробной информации о товаре"""
    current_product = Product.objects.get(pk=pk)
    context = {'current_product' : current_product}
    return render(request, 'product_details.html', context=context)

