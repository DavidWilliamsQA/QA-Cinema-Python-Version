def test_login_user(test_user, client):
    res = client.post(
        "/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"],
        },
    )
    assert res.status_code == 200


def test_unauthorized_login_user(client):
    res = client.post(
        "/login",
        data={
            "username": "wrongemail@test.com",
            "password": "wrongpassword",
        },
    )
    assert res.status_code == 403
