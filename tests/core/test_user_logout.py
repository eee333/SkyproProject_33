import pytest

from core.models import User


@pytest.mark.django_db
def test_logout(client, logged_in_user):
    username = "test_username_3"
    password = "string2yuyt"

    response_1 = client.get(
        "/core/profile",
    )
    response_2 = client.delete(
        "/core/profile"
    )
    response_3 = client.get(
        "/core/profile",
    )
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 403

