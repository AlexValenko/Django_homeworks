from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, UpdateView
from django.views.generic.edit import CreateView

from .forms import FeedbackForm, ProductForm
from .models import Category, Product


class HomeListView(ListView):
    """Класс CBV для отображения домашней страницы - отображает последние 6 добавленных товаров"""

    model = Product
    template_name = "home.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.order_by("-created_at")[:6]


class ContactsFormView(FormView):
    """Класс CBV для отправки страницы Контакты, и получения формы обратной связи"""

    template_name = "contacts.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("catalog:home")  # Перенаправление на домашнюю страницу

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]
        print(f'Получена обратная связь от {name} ({phone}). Текст сообщения "{message}"')
        return super().form_valid(form)


class ProductDetailView(DetailView):
    """Класс для отображения подробной информации о товаре product_details"""

    model = Product
    template_name = "product_details.html"


class ProductCreateView(CreateView):
    """Класс для заполнения данных о новом товаре"""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

class ProductUpdateView(UpdateView):
    """Класс для редактирования данных о товаре"""
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductListView(ListView):
    """Класс - контроллер для вывода страницы с товарами (весь каталог товаров)"""

    model = Product
    template_name = "products.html"
    ordering = "category__category_name"
    paginate_by = 9
