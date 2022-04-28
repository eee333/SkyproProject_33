from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User


class UserAdmin(BaseUserAdmin):
    # exclude = ("password",)
    list_display = ("username", "email", "first_name", "last_name")
    readonly_fields = ("date_joined", "last_login")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "is_superuser")
    # fieldsets = BaseUserAdmin.fieldsets + ((None, {'fields': ('type',)}),)
    # add_fieldsets = BaseUserAdmin.add_fieldsets + ((None, {'fields': ('type',)}),)


admin.site.register(User, UserAdmin)
