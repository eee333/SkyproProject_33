import pytest


@pytest.mark.django_db
def test_update_profile(client, logged_in_user):

    data = {
        "username": "test_username_updated",
        "first_name": "first_name_updated",
        "last_name": "last_name_updated",
        "email": "updated@example.com"
    }
    expected_response = {
        "id": logged_in_user.id,
        "username": "test_username_updated",
        "first_name": "first_name_updated",
        "last_name": "last_name_updated",
        "email": "updated@example.com"
    }
    response = client.patch(
        "/core/profile",
        data,
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data == expected_response
