from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    """Функция для отправки домашней страницы"""

    latest_products = Product.objects.order_by('created_at')[:5]
    print("Топ-5 последних товаров")
    if latest_products:
        for product in latest_products:
            print(f'Товар: {product.prod_name}, Цена: {product.price}, Дата создания: {product.created_at}')

    return render(request, "home.html")


def contacts(request):
    """Метод для отправки страницы Контакты, и получения формы обратной связи"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'Получена обратная связь от {name} ({phone}). Текст сообщения "{message}"')
        return HttpResponse(f"Спасибо, {name}! сообщение получено.")
    return render(request, "contacts.html")
