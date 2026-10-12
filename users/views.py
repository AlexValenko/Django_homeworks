from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER

from .forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    """Контроллер для регистрации нового пользователя"""

    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [user_email]
        send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER, recipient_list=recipient_list)


class CustomLogoutView(LogoutView):
    template_name = "logged_out.html"
