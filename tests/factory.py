from freezegun import freeze_time

import factory
from core.models import User
from goals.models import Board, BoardParticipant


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test_username_3"
    first_name = "test_first_name"
    last_name = "test_last_name"
    email = "test@example.com"
    # password = "string2yuyt"
    password = "pbkdf2_sha256$320000$HMJhEzN4sbOpphoPJnEjwp$DQkPE/7yyMHE66qMt/pqX2kAaGZHYT/sg9loithgeNk="


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    # title = "test_board_2"
    title = factory.Faker("name")


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    """Role:
        OWNER = 1, "Владелец"
        WRITER = 2, "Редактор"
        READER = 3, "Читатель"
        """

    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)
    role = 1
