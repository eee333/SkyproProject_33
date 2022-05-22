import pytest


@pytest.fixture()
@pytest.mark.django_db
def logged_in_user(client, user):

    password = "string2yuyt"

    response = client.post(
        "/core/login",
        {"username": user.username, "password": password},
        format="json"
    )

    return user
