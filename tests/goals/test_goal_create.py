import pytest
from freezegun import freeze_time


@freeze_time("2022-05-05T05:00:00")
@pytest.mark.django_db
def test_goal_create(client, logged_in_user, category_1):

    data = {
        "title": "test_goal",
        "category": category_1.id,
        "description": "test_description",
        "due_date": "2022-06-05",
        "status": 1,
        "priority": 1
    }
    expected_response = {
        "title": "test_goal",
        "category": category_1.id,
        "description": "test_description",
        "due_date": "2022-06-05",
        "status": 1,
        "priority": 1,
        "created": "2022-05-05T05:00:00Z",
        "updated": "2022-05-05T05:00:00Z"
    }

    response = client.post(
        "/goals/goal/create",
        data,
        content_type="application/json"
    )

    new_goal_id = response.data.pop("id")
    assert response.status_code == 201
    assert response.data == expected_response
