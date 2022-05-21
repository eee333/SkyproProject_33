import pytest


@pytest.mark.django_db
def test_update_password(client, logged_in_user):
    old_password = "test_pass"
    new_password = "test_pass_342"
    username = "test_user"
    data = {
        "old_password": old_password,
        "new_password": new_password
    }

    response = client.patch(  # change password
        "/core/update_password",
        data,
        content_type="application/json"
    )
    response_2 = client.get(  # check logout
        "/core/profile",
    )
    response_3 = client.post(  # login
        "/core/login",
        {"username": username, "password": new_password},
        format="json"
    )

    expected_response = {
        "username": username,
        "first_name": "",
        "last_name": "",
        "email": ""
    }

    assert response.status_code == 200
    assert response_2.status_code == 403
    assert response_3.status_code == 200
    assert type(response_3.data.pop("id")) == int
    assert response_3.data == expected_response
