from django.db import models


class Category(models.Model):
    """Модель для описания категорий товаров"""

    category_name = models.CharField(
        max_length=150, verbose_name="Категория", unique=True, help_text="Наименование категории"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание", help_text="Описание категории")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "category_name",
        ]


class Product(models.Model):
    """Модель для описания продаваемых товаров"""

    prod_name = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Наименование продукта"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание", help_text="Описание продукта")
    prod_image = models.ImageField(upload_to="images/", verbose_name="Изображение товара", null=True, blank=True)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True,
        verbose_name="Категория товара",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена товара", help_text="Цена товара", null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["prod_name", "price", "category", "created_at"]
