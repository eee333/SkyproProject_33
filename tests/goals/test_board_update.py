import pytest
from freezegun import freeze_time

from goals.serializers import BoardParticipantSerializer


@freeze_time("2022-05-05T05:00:00")
@pytest.mark.django_db
def test_board_update(client, logged_in_user, board_participant_1):

    participants = [BoardParticipantSerializer(board_participant_1).data]
    data = {
        "title": "test_board_updated"
    }
    expected_response = {
        "id": board_participant_1.board.id,
        "title": "test_board_updated",
        "updated": "2022-05-05T05:00:00Z",
        "participants": participants,
        "is_deleted": False
    }

    response = client.patch(
        f"/goals/board/{board_participant_1.board.id}",
        data,
        content_type="application/json"
    )

    assert response.status_code == 200
    created = response.data.pop("created")
    assert response.data == expected_response
