import pytest

from core.serializers import UserSerializer
from tests.factory import GoalFactory


@pytest.mark.django_db
def test_goal_get(client, logged_in_user, category_1):
    user = UserSerializer(logged_in_user).data
    goal = GoalFactory(category=category_1, user=logged_in_user)
    expected_response = {
        "id": goal.id,
        "title": goal.title,
        "user": user,
        "category": category_1.id,
        "description": goal.description,
        "due_date": "2022-06-05",
        "status": 1,
        "priority": 1
    }

    response = client.get(
        f"/goals/goal/{goal.id}"
    )

    assert response.status_code == 200
    created = response.data.pop("created")
    updated = response.data.pop("updated")
    assert response.data == expected_response
