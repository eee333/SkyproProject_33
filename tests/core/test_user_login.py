import pytest

from core.models import User


@pytest.mark.django_db
def test_login(client, django_user_model):
    username = "test_user"
    password = "1234"

    user = django_user_model.objects.create_user(
        username=username, password=password
    )

    expected_response = {
        "id": user.id,
        "username": "test_user",
        "first_name": "",
        "last_name": "",
        "email": ""
    }

    response = client.post(
        "/core/login",
        {"username": username, "password": password},
        format="json"
    )

    assert response.status_code == 200
    assert response.data == expected_response
