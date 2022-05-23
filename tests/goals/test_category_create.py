import pytest
from freezegun import freeze_time

from goals.models import BoardParticipant, GoalCategory


@freeze_time("2022-05-05T05:00:00")
@pytest.mark.django_db
def test_category_create(client, logged_in_user, board_participant_1):

    data = {
        "title": "test_category",
        "board": board_participant_1.board.id
    }
    expected_response = {
        "title": "test_category",
        "created": "2022-05-05T05:00:00Z",
        "updated": "2022-05-05T05:00:00Z",
        "is_deleted": False,
        "board": board_participant_1.board.id
    }

    response = client.post(
        "/goals/goal_category/create",
        data,
        content_type="application/json"
    )

    new_category_id = response.data.pop("id")
    assert response.status_code == 201
    assert response.data == expected_response
    assert GoalCategory.objects.get(pk=new_category_id).title == "test_category"
