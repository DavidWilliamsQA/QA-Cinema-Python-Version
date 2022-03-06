from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from app.database import get_db, Base
from app.oauth2 import create_access_token
from app import models
import json
import pytest

load_dotenv()


SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST_NAME')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DATABASE_NAME')}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(authorized_client):
    user_data = {"email": "test2@test.com", "password": "password123"}
    res = authorized_client.post("/users/", json=user_data)

    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def test_user_create(test_users, client):
    new_user = test_users[1]

    return new_user


@pytest.fixture
def token(test_user_create):
    return create_access_token(
        {"user_id": test_user_create.id, "admin_status": test_user_create.admin}
    )


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}

    return client


@pytest.fixture
def test_movies(session):
    movie_data = [
        {"status": "Testing", "api_ID": 5, "rating": "yess"},
        {"status": "Testing", "api_ID": 5, "rating": "yess"},
        {"status": "Testing", "api_ID": 5, "rating": "yess"},
        {"status": "Testing", "api_ID": 5, "rating": "yess"},
    ]

    def create_movie_model(movie):
        return models.Movie(**movie)

    movie_map = map(create_movie_model, movie_data)
    movies = list(movie_map)

    session.add_all(movies)
    session.commit()

    movie_query = session.query(models.Movie).all()
    return movie_query


@pytest.fixture
def test_showtime(session):
    showtime_data = [
        {"time": "08/09/2021 12:30"},
        {"time": "05/11/2020 10:30"},
        {"time": "11/04/2020 15:30"},
    ]

    def create_showtime_model(showtime):
        return models.ShowTime(**showtime)

    showtime_map = map(create_showtime_model, showtime_data)
    showtimes = list(showtime_map)

    session.add_all(showtimes)
    session.commit()

    showtime_query = session.query(models.ShowTime).all()
    return showtime_query


@pytest.fixture
def test_users(session):
    users_data = [
        {"email": "test1@test.com", "password": "password123", "admin": False},
        {"email": "test@test.com", "password": "password123", "admin": True},
        {"email": "test3@test.com", "password": "password123", "admin": False},
    ]

    def create_users_model(users):
        return models.User(**users)

    users_map = map(create_users_model, users_data)
    users = list(users_map)

    session.add_all(users)
    session.commit()

    users_query = session.query(models.User).all()
    return users_query


@pytest.fixture
def test_movie_showtimes(session, test_showtime, test_movies):
    showtimes_data = [
        {"movie_id": 1, "showtime_id": 3},
        {"movie_id": 4, "showtime_id": 1},
        {"movie_id": 3, "showtime_id": 2},
    ]

    def create_movie_showtimes_model(showtimes):
        return models.MovieShowTimes(**showtimes)

    showtimes_map = map(create_movie_showtimes_model, showtimes_data)
    showtimes = list(showtimes_map)

    session.add_all(showtimes)
    session.commit()

    showtimes_query = session.query(models.MovieShowTimes).all()
    return showtimes_query


@pytest.fixture
def test_comments(session):
    comment_data = [
        {
            "movieTitle": "Test Title 1",
            "customerName": "Jane Doe",
            "rating": 4,
            "comment": "Bad movie",
        },
        {
            "movieTitle": "Test Title 2",
            "customerName": "John Smith",
            "rating": 6,
            "comment": "Average movie",
        },
        {
            "movieTitle": "Test Title 2",
            "customerName": "Joshua Donner",
            "rating": 10,
            "comment": "Awesome movie bro",
        },
    ]

    def create_comments_model(comments):
        return models.Comment(**comments)

    comment_map = map(create_comments_model, comment_data)
    comments = list(comment_map)

    session.add_all(comments)
    session.commit()

    comment_query = session.query(models.Comment).all()
    return comment_query


@pytest.fixture
def test_bookings(session):
    booking_data = [
        {
            "movieName": "Movie1",
            "movieId": 1,
            "totalPrice": 2.0,
            "phoneNumber": "07458796587",
            "adultNo": 3,
            "childNo": 2,
            "dateTime": "12/12/22",
            "emailAddress": "test1@test.com",
            "customerName": "test1",
            "studentNo": 2,
        },
        {
            "movieName": "Movie2",
            "movieId": 2,
            "totalPrice": 2.0,
            "phoneNumber": "07458796587",
            "adultNo": 2,
            "childNo": 2,
            "dateTime": "12/12/22",
            "emailAddress": "test2@test.com",
            "customerName": "test2",
            "studentNo": 2,
        },
        {
            "movieName": "Movie3",
            "movieId": 3,
            "totalPrice": 15.0,
            "phoneNumber": "07458796587",
            "adultNo": 2,
            "childNo": 3,
            "dateTime": "12/12/22",
            "emailAddress": "test3@test.com",
            "customerName": "test3",
            "studentNo": 2,
        },
        {
            "movieName": "Movie4",
            "movieId": 4,
            "totalPrice": 28.0,
            "phoneNumber": "07458796587",
            "adultNo": 5,
            "childNo": 2,
            "dateTime": "12/12/22",
            "emailAddress": "test4@test.com",
            "customerName": "test4",
            "studentNo": 2,
        },
    ]

    def create_booking_model(booking):
        return models.Booking(**booking)

    booking_map = map(create_booking_model, booking_data)
    bookings = list(booking_map)

    session.add_all(bookings)
    session.commit()

    booking_query = session.query(models.Booking).all()
    return booking_query
