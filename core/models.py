from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Админ"),
    ]

    email = models.EmailField(null=True)
    role = models.CharField(max_length=9, choices=ROLES, default="member")
    # age = models.PositiveIntegerField(null=True)
    birth_date = models.DateField(null=True, default="2000-01-01")
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
