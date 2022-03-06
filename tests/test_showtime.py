def test_create_showtime(authorized_client):
    res = authorized_client.post("/showTime/", json={"time": "05/09/2020 12:30"})
    assert res.status_code == 200


def test_get_showtime(client):
    res = client.get("/showTime/")
    assert res.status_code == 200


def test_delete_showtime(authorized_client, test_showtime):
    res = authorized_client.delete(f"/showTime/{test_showtime[0].id}")
    assert res.status_code == 204
