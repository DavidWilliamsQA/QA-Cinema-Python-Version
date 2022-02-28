def test_root(client):
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Welcome to my QA Cinema App Backend"


def test_create_movie(client):
    res = client.post(
        "/movies/", json={"status": "Test", "api_ID": 3, "rating": "3 stars"}
    )
    print(res.json())


def test_login_user(client):
    res = client.post(
        "/login", data={"username": "test@test.com", "password": "password123"}
    )
    assert res.status_code == 200
