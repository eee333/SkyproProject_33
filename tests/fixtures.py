import pytest

from goals.models import Board, BoardParticipant
from tests.factory import UserFactory, BoardFactory, ParticipantFactory


@pytest.fixture()
@pytest.mark.django_db
def logged_in_user(client):
    user = UserFactory()
    password = "string2yuyt"

    response = client.post(
        "/core/login",
        {"username": user.username, "password": password},
        format="json"
    )

    return user


@pytest.fixture()
@pytest.mark.django_db
def board_participant_1(client, logged_in_user):
    data = {
        "title": "test_board_1"
    }
    board = BoardFactory(title="test_board_1")
    board_participant = ParticipantFactory(
        board=board,
        user=logged_in_user,
        role=1
    )

    # response = client.post(
    #     "/goals/board/create",
    #     data,
    #     content_type="application/json"
    # )

    return board_participant
