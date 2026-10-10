from django.contrib.auth.views import LoginView

from users.forms import CustomAuthenticationForm
from users.views import UserRegisterView, CustomLogoutView

from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="login.html", authentication_form=CustomAuthenticationForm),
        name="login",
    ),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
