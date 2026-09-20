from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .models import Category, Product


class HomeListView(ListView):
    """Контроллер для отображения домашней страницы CBV - отображает последние 6 добавленных товаров"""
    model = Product
    template_name = "home.html"
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by("-created_at")[:6]


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
    context = {"current_product": current_product}
    return render(request, "product_details.html", context=context)


def add_product(request):
    """Контроллер для заполнения данных о новом товаре"""
    categories = Category.objects.all()

    if request.method == "POST":
        Product.objects.create(
            prod_name=request.POST.get("prod_name"),
            description=request.POST.get("description"),
            category_id=request.POST.get("category"),
            price=request.POST.get("price"),
            prod_image=request.FILES.get("prod_image"),
        )
        print(f"Товар {request.POST.get('prod_name')} успешно добавлен в базу")
        return redirect("/home/")

    context = {"categories": categories}
    return render(request, "add_product.html", context=context)


def products(request):
    """Контроллер для вывода страницы с товарами (весь каталог товаров)"""
    all_products = Product.objects.all().order_by("category")

    paginator = Paginator(all_products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "products.html", context=context)
