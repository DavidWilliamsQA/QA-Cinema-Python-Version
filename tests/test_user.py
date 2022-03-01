def test_login_user(client):
    res = client.post(
        "/login", data={"username": "test@test.com", "password": "password123"}
    )
    assert res.status_code == 200