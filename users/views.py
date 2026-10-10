from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomUserCreationForm


class UserRegisterView(View):
    """Контроллер для регистрации нового пользователя"""

    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def get(self, request):
        """Показывает пустую форму регистрации"""
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        """Обрабатывает отправленную форму"""
        form = self.form_class(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})


class CustomLogoutView(LogoutView):
    template_name = "logged_out.html"
