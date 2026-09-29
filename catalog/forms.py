from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import filesizeformat

from catalog.models import Product

STOP_PRODUCT_LIST = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]
ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png"]


class FeedbackForm(forms.Form):
    """Класс для формы обратной связи"""

    name = forms.CharField(max_length=100, label="Имя", required=True)
    phone = forms.CharField(max_length=50, label="Телефон", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Сообщение", required=True)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "created_at",
            "updated_at",
        ]

    # Стилизация
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["prod_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите название продукта",
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите описание продукта",
            }
        )

        self.fields["prod_image"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Загрузите изображение",
            }
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите цену товара",
            }
        )

    # Валидация
    def clean_prod_name(self):
        """Метод для валидации названия продукта - не должно содержать запрещенных слов из STOP_PRODUCT_LIST"""
        prod_name = self.cleaned_data.get("prod_name")
        lower_name = prod_name.strip().lower()
        for stop_word in STOP_PRODUCT_LIST:
            if stop_word in lower_name:
                raise ValidationError(message="Название продукта не должно содержать запрещённых слов.")
        return prod_name

    def clean_description(self):
        """Метод для валидации описания - не должно содержать запрещенных слов из STOP_PRODUCT_LIST"""
        description = self.cleaned_data.get("description")
        lower_description = description.strip().lower()
        for stop_word in STOP_PRODUCT_LIST:
            if stop_word in lower_description:
                raise ValidationError(message="Описание не должно содержать запрещённых слов.")
        return description

    def clean_price(self):
        """Метод для валидации цены товара > 0"""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError(message="Цена товара должна быть положительным числом")
        return price

    def clean_prod_image(self):
        """Валидация для изображения - проверка размера и расширения"""
        image = self.cleaned_data.get("prod_image")
        if not image:
            return image

        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise ValidationError(
                f"Размер файла слишком большой. Максимальный размер — 5 МБ. "
                f"Текущий размер: {filesizeformat(image.size)}"
            )
        """При попытке загрузить файл не изображения, например doc - будет применена встроенная валидация модели
        (prod_image = models.ImageField), и будет выведено другое сообщение об ошибке"""
        validator = FileExtensionValidator(
            allowed_extensions=ALLOWED_EXTENSIONS, message="Разрешены только файлы форматов JPG/JPEG или PNG."
        )
        validator(image)
