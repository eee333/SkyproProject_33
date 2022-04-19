from django.db import models

from django.contrib.auth.models import AbstractUser

from core.managers import UserManager


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    objects = UserManager()
