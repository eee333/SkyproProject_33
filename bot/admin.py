from django.contrib import admin

from bot.models import TgUser


class TgUserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "username_tg", "user")
    readonly_fields = ["verification_code",]


admin.site.register(TgUser, TgUserAdmin)
