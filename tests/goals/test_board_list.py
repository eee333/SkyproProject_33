import pytest
from freezegun import freeze_time

from goals.models import BoardParticipant
from goals.serializers import BoardParticipantSerializer, BoardListSerializer
from tests.factory import BoardFactory, ParticipantFactory


@pytest.mark.django_db
def test_board_list(client, logged_in_user):
    boards = BoardFactory.create_batch(3)
    boards.sort(key=lambda x: getattr(x, 'title'))
    for board in boards:
        ParticipantFactory(
            board=board,
            user=logged_in_user,
            role=1
        )

    expected_response = BoardListSerializer(boards, many=True).data

    response = client.get(
        "/goals/board/list"
    )

    assert response.status_code == 200
    assert response.data == expected_response
