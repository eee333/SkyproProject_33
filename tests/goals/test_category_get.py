import pytest

from core.serializers import UserSerializer


@pytest.mark.django_db
def test_category_get(client, logged_in_user, category_1):
    user = UserSerializer(logged_in_user).data
    expected_response = {
        "id": category_1.id,
        "title": category_1.title,
        "user": user,
        "is_deleted": False,
        "board": category_1.board.id
    }

    response = client.get(
        f"/goals/goal_category/{category_1.id}"
    )

    assert response.status_code == 200
    created = response.data.pop("created")
    updated = response.data.pop("updated")
    assert response.data == expected_response
