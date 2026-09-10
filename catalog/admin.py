from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category_name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "prod_name",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "prod_name",
        "description",
    )
