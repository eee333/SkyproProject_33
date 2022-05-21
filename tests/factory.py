import factory
from core.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test_username_3"
    first_name = "test_first_name"
    last_name = "test_last_name"
    email = "test@example.com"
    password = "string2yuyt"
