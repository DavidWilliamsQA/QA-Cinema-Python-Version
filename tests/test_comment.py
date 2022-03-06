def test_create_comment(client):
    res = client.post(
        "/comments/",
        json={
            "movieTitle": "Test Title 1",
            "customerName": "John Doe",
            "rating": 2,
            "comment": "Bad movie",
        },
    )

    assert res.status_code == 200


def test_get_comment(client, test_comments):
    res = client.get(f"/comments/{test_comments[0].id}")
    assert res.status_code == 200


def test_delete_comment(authorized_client, test_comments):
    res = authorized_client.delete(f"/comments/{test_comments[1].id}")
    assert res.status_code == 204


def test_get_all_comments(client, test_comments):
    res = client.get("/comments/")
    assert res.status_code == 200
