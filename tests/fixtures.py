import pytest


@pytest.fixture()
@pytest.mark.django_db
def csrf_token(client, django_user_model):
    username = "test_user"
    password = "test_pass"

    django_user_model.objects.create_user(
        username=username, password=password
    )

    response = client.post(
        "/core/login",
        {"username": username, "password": password},
        format="json"
    )

    return response.get_signed_cookie("csrftoken")
