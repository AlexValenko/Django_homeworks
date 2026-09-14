from itertools import product

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category


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

def add_product(request):
    """Контроллер для заполнения данных о новом товаре"""
    categories = Category.objects.all()

    if request.method == "POST":
        # Создаём объект товара из данных формы
        Product.objects.create(
            prod_name=request.POST.get("prod_name"),
            description=request.POST.get("description"),
            category_id=request.POST.get("category"),
            price=request.POST.get("price"),
            prod_image=request.FILES.get("prod_image"),  # файлы берём из request.FILES
        )
        # После сохранения — возврат на главную
        return redirect("/home/")

    context = {'categories' : categories}
    return render(request, 'add_product.html', context=context)


