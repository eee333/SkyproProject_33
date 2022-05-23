import pytest
from freezegun import freeze_time

from goals.models import BoardParticipant


@freeze_time("2022-05-05T05:00:00")
@pytest.mark.django_db
def test_board_create(client, logged_in_user):

    data = {
        "title": "test_board"
    }
    expected_response = {
        "title": "test_board",
        "created": "2022-05-05T05:00:00Z",
        "updated": "2022-05-05T05:00:00Z",
        "is_deleted": False
    }

    response = client.post(
        "/goals/board/create",
        data,
        content_type="application/json"
    )

    new_board_id = response.data.pop("id")
    assert response.status_code == 201
    assert response.data == expected_response
    assert BoardParticipant.objects.filter(board_id=new_board_id).exists()
