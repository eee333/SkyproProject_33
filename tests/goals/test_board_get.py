import pytest
from freezegun import freeze_time

from goals.models import BoardParticipant
from goals.serializers import BoardParticipantSerializer
from tests.factory import BoardFactory


@pytest.mark.django_db
def test_board_get(client, logged_in_user, board_participant_1):

    participants = [BoardParticipantSerializer(board_participant_1).data]

    expected_response = {
        "id": board_participant_1.board.id,
        "title": board_participant_1.board.title,
        "participants": participants,
        "is_deleted": False
    }

    response = client.get(
        f"/goals/board/{board_participant_1.board.id}"
    )

    assert response.status_code == 200
    created = response.data.pop("created")
    updated = response.data.pop("updated")
    assert response.data == expected_response
