from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, FormView, ListView, UpdateView
from django.views.generic.edit import CreateView

from .forms import FeedbackForm, ProductForm
from .models import Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Класс для отображения подробной информации о товаре product_details"""

    model = Product
    template_name = "product_details.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для заполнения данных о новом товаре"""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования данных о товаре"""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления продукта"""

    model = Product
    template_name = "product_confirm_delete.html"

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.has_perm("catalog.can_unpublish_product"):
            return Product.objects.all()

        return Product.objects.filter(owner=user)

    def get_success_url(self):
        return reverse_lazy("catalog:home")


class ProductListView(ListView):
    """Класс - контроллер для вывода страницы с товарами (весь каталог товаров)"""

    model = Product
    template_name = "products.html"
    ordering = "category__category_name"
    paginate_by = 9


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
