def test_create_user(authorized_client):
    res = authorized_client.post(
        "/users/",
        json={
            "email": "createdtestuser@test.com",
            "password": "createdtestuserpassword123",
        },
    )
    assert res.status_code == 200


def test_unauthorised_create_user(client):
    res = client.post(
        "/users/",
        json={
            "email": "createdtestuser@test.com",
            "password": "createdtestuserpassword123",
        },
    )
    assert res.status_code == 401


def test_get_user(client, test_users):
    res = client.get(f"/users/{test_users[0].id}")
    assert res.status_code == 200


def test_delete_user(authorized_client, test_users):
    res = authorized_client.delete(f"/users/{test_users[0].id}")
    assert res.status_code == 204


def test_unauthorised_delete_user(client, test_users):
    res = client.delete(f"/users/{test_users[0].id}")
    assert res.status_code == 401


def test_get_all_user(authorized_client, test_users):
    res = authorized_client.get(f"/users/")
    assert res.status_code == 200


def test_unauthorised_get_all_user(client, test_users):
    res = client.get(f"/users/")
    assert res.status_code == 401
