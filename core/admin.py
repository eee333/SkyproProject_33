from django.contrib import admin
from core.models import User


class UserAdmin(admin.ModelAdmin):
    # exclude = ("password",)
    list_display = ("username", "email", "first_name", "last_name")
    readonly_fields = ("date_joined", "last_login")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "is_superuser")


admin.site.register(User, UserAdmin)
