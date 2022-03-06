def test_create_user(authorized_client, client):
    res = authorized_client.post(
        "/users/",
        json={
            "email": "createdtestuser@test.com",
            "password": "createdtestuserpassword123",
        },
    )
    assert res.status_code == 200


def test_get_user():
    pass


def test_delete_user():
    pass
