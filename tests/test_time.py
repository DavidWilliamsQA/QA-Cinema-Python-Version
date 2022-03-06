def test_delete_time(authorized_client, test_movie_showtimes):
    res = authorized_client.delete(
        f"/time/deleteMovieShowtime", json={"movie_id": 1, "showtime_id": 3}
    )
    assert res.status_code == 204


def test_set_time(authorized_client, test_movie_showtimes):
    res = authorized_client.post(
        f"/time/setMovieShowtime", json={"movie_id": 4, "showtime_id": 3}
    )
    assert res.status_code == 200


def test_unauthorized_delete_time(client, test_movie_showtimes):
    res = client.delete(
        f"/time/deleteMovieShowtime", json={"movie_id": 1, "showtime_id": 3}
    )
    assert res.status_code == 401


def test_unauthorized_set_time(client, test_movie_showtimes):
    res = client.post(f"/time/setMovieShowtime", json={"movie_id": 4, "showtime_id": 3})
    assert res.status_code == 401
