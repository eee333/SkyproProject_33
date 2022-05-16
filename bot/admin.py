from django.contrib import admin


class TgUserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "user_ud", "user")

