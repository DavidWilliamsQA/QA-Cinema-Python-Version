from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP, Boolean, Column, Float, ForeignKey, Integer, String
from .database import Base


class MovieShowTimes(Base):
    __tablename__ = "movie_showTimes"
    movie_id = Column("movie_id", ForeignKey("movie.id"), primary_key=True)
    showtime_id = Column("showtime_id", ForeignKey("showTime.id"), primary_key=True)


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    api_ID = Column(Integer, nullable=False)
    rating = Column(String, nullable=False)
    showTimes = relationship(
        "ShowTime", secondary="movie_showTimes", back_populates="movies"
    )


class ShowTime(Base):
    __tablename__ = "showTime"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    movies = relationship(
        "Movie", secondary="movie_showTimes", back_populates="showTimes"
    )


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movieId = Column(
        Integer, ForeignKey("movie.id", ondelete="CASCADE"), nullable=False
    )
    movieName = Column(String, nullable=False)
    dateTime = Column(String, nullable=False)
    totalPrice = Column(Float, nullable=False)
    emailAddress = Column(String, nullable=False)
    phoneNumber = Column(String, nullable=False)
    customerName = Column(String, nullable=False)
    adultNo = Column(Integer, nullable=False)
    studentNo = Column(Integer, nullable=False)
    childNo = Column(Integer, nullable=False)
    movie = relationship("Movie")


class Response(Base):
    __tablename__ = "response"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Boolean, nullable=False)
    details = Column(String, nullable=False)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movieTitle = Column(String, nullable=False)
    customerName = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)


class Email(Base):
    __tablename__ = "email"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customerName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    admin = Column(String, nullable=False, default=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
