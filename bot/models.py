from django.db import models

from core.models import User


class TgUser(models.Model):
    class Meta:
        verbose_name = "TG User"
        verbose_name_plural = "TG Users"

    chat_id = models.PositiveBigIntegerField(unique=True)
    user_ud = models.CharField(unique=True, max_length=255, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)

    def __str__(self):
        if self.user_ud:
            return self.user_ud
        elif self.user and self.user.username:
            return self.user.username
        else:
            return super().__str__()


