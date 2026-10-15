from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import User

from config.settings import EMAIL_HOST_USER, DEBUG


class UserRegisterView(CreateView):
    """Контроллер для регистрации нового пользователя"""

    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)

        # Отключаем функционал отправки письма для режима DEBUG
        if not DEBUG:
            self.send_welcome_email(user.email)
        return response

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [user_email]
        send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER, recipient_list=recipient_list)


class CustomLogoutView(LogoutView):
    template_name = "logged_out.html"


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования профиля пользователя."""

    model = User
    form_class = CustomUserUpdateForm
    template_name = "profile_form.html"
    success_url = reverse_lazy("users:profile_update")

    def get_object(self, queryset=None):
        """Возвращает профиль текущего пользователя."""
        return self.request.user