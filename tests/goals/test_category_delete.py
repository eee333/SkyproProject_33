import pytest

from goals.models import GoalCategory


@pytest.mark.django_db
def test_category_delete(client, logged_in_user, category_1):

    response = client.delete(
        f"/goals/goal_category/{category_1.id}"
    )

    assert response.status_code == 204
    assert GoalCategory.objects.get(pk=category_1.id).is_deleted
