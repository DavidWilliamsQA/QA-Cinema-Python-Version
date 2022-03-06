def test_create_booking(client, test_movies):
    res = client.post(
        "/booking/",
        json={
            "movieName": "Movie2",
            "movieId": 2,
            "totalPrice": 2.0,
            "phoneNumber": "07458796587",
            "adultNo": 2,
            "childNo": 2,
            "dateTime": "12/12/22",
            "emailAddress": "test@test.com",
            "customerName": "test",
            "studentNo": 2,
        },
    )
    assert res.status_code == 200


def test_get_booking_by_id(client, test_movies, test_bookings):
    res = client.get(f"/booking/{test_bookings[0].id}")
    assert res.status_code == 200


def test_delete_booking(authorized_client, test_movies, test_bookings):
    res = authorized_client.delete(f"/booking/{test_bookings[0].id}")
    assert res.status_code == 204


def test_unauthorised_delete_booking(client, test_movies, test_bookings):
    res = client.delete(f"/booking/{test_bookings[1].id}")
    assert res.status_code == 401
