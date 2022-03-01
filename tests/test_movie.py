def test_create_movie(client):
    res = client.post(
        "/movies/", json={"status": "Test", "api_ID": 3, "rating": "3 stars"}
    )
    print(res.json())


def test_delete_movie(client):
    pass


def test_get_movie_by_id(client):
    pass


def test_get_all_movies(client):
    pass
