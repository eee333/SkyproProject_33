import pytest

from goals.serializers import GoalCategorySerializer
from tests.factory import CategoryFactory, UserFactory, ParticipantFactory


@pytest.mark.django_db
def test_category_list(client, logged_in_user, board_participant_1):
    categories = CategoryFactory.create_batch(3, user=logged_in_user, board=board_participant_1.board)
    user_2 = UserFactory(username="test_username_4")
    board_2 = ParticipantFactory(user=user_2)
    categories_2 = CategoryFactory.create_batch(3, user=user_2, board=board_2.board)  # Should be skipped
    categories.sort(key=lambda x: getattr(x, 'title'))

    expected_response = GoalCategorySerializer(categories, many=True).data

    response = client.get(
        "/goals/goal_category/list"
    )

    assert response.status_code == 200
    assert response.data == expected_response
