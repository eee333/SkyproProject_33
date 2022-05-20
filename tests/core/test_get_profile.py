import pytest


@pytest.mark.django_db
def test_get_profile(client, logged_in_user):

    expected_response = {
        "id": logged_in_user.id,
        "username": "test_user",
        "first_name": "",
        "last_name": "",
        "email": ""
    }

    response = client.get(
        "/core/profile",
    )

    assert response.status_code == 200
    assert response.data == expected_response
