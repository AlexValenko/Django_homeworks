from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации пользователя на сайте"""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "phone_number",
            "avatar",
            "user_country",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    # Стилизация
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите Email (обязательное поле)",
            }
        )

        self.fields["phone_number"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите номер телефона (необязательно)",
            }
        )

        self.fields["avatar"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Загрузите изображение (необязательно)",
            }
        )

        self.fields["user_country"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите название вашей страны (необязательно)",
            }
        )

        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите Ваше имя (необязательно)",
            }
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите Вашу фамилию (необязательно)",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Повторите пароль",
            }
        )


class CustomAuthenticationForm(AuthenticationForm):
    """Форма аутентификации"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите Email",
            }
        )

        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        )
