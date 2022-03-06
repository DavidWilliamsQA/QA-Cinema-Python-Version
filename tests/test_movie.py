def test_create_movie(authorized_client):
    res = authorized_client.post(
        "/movies/", json={"status": "Test", "api_ID": 3, "rating": "3 stars"}
    )
    assert res.status_code == 200


def test_delete_movie(authorized_client, test_movies):
    res = authorized_client.delete(f"/movies/{test_movies[0].id}")
    assert res.status_code == 204


def test_get_movie_by_id(client, test_movies):
    res = client.get(f"/movies/{test_movies[0].id}")
    assert res.status_code == 200


def test_get_all_movies(client):
    res = client.get(f"/movies/")
    assert res.status_code == 200
