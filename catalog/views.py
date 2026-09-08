from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Функция для отправки домашней страницы"""
    return render(request, "home.html")


def contacts(request):
    """Метод для отправки страницы Контакты, и получения формы обратной связи"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f'Получена обратная связь от {name} ({phone}). Текст сообщения "{message}"'
        )
        return HttpResponse(f"Спасибо, {name}! сообщение получено.")
    return render(request, "contacts.html")
