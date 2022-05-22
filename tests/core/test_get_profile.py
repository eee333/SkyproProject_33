import pytest


@pytest.mark.django_db
def test_get_profile(client, logged_in_user):

    expected_response = {
        "id": logged_in_user.id,
        "username": "test_username_3",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "test@example.com"
    }

    response = client.get(
        "/core/profile",
    )

    assert response.status_code == 200
    assert response.data == expected_response
