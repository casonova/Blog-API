from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "username",
        "name",
        "password",
        "action_choice",
        "created_date",
        "updated_date",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    search_fields = ["email"]
