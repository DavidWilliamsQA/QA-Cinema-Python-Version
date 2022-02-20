from time import time

from sqlalchemy import engine
from .models import Movie, ShowTime
from sqlalchemy.orm import Session
from .database import get_db
from fastapi import Depends

# Insert data


def populate_db(db):
    with Session(bind=engine) as session:
        movie1 = Movie(status="Movie 1", api_ID=555, rating="5 stars")
        movie2 = Movie(status="Movie 2", api_ID=5232, rating="2 stars")

        showTime1 = ShowTime(time="06/10/2020 12:30")
        showTime2 = ShowTime(time="05/07/2020 12:30")
        showTime3 = ShowTime(time="12/03/2020 12:30")

        movie1.showTimes = [showTime1, showTime2]
        movie2.showTimes = [showTime1, showTime3]

        db.add_all([movie1, movie2, showTime1, showTime2, showTime3])
        db.commit()
