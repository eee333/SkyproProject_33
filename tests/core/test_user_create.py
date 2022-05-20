import pytest


def test_root_not_found(client):
    response = client.get("/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_create(client):

    data = {
        "username": "test_username",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string2yuyt",
        "password_repeat": "string2yuyt"
    }
    expected_response = {
        "username": "test_username",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com"
    }

    response = client.post(
        "/core/signup",
        data,
        format="json"
    )

    assert response.status_code == 201
    assert type(response.data.pop("id")) == int
    assert response.data == expected_response


@pytest.mark.django_db
def test_simple_pass_user_create(client):

    data = {
        "username": "test_username",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "1234",
        "password_repeat": "1234"
    }

    response = client.post(
        "/core/signup",
        data,
        format="json"
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_not_same_pass_user_create(client):

    data = {
        "username": "test_username",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string2yuyt111",
        "password_repeat": "string2yuyt"
    }

    response = client.post(
        "/core/signup",
        data,
        format="json"
    )

    assert response.status_code == 400
