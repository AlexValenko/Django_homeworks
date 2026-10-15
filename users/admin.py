from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "date_joined",
        "first_name",
        "last_name",
        "user_country",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("date_joined",)
    search_fields = ("email",)
