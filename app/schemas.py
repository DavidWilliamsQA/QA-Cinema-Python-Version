from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class ShowTimes(BaseModel):
    id: Optional[int]
    time: str

    class Config:
        orm_mode = True


class Movie(BaseModel):
    status: str
    api_ID: int
    rating: str
    showTimes: Optional[List[ShowTimes]] = []

    class Config:
        orm_mode = True


class MovieOut(Movie):
    id: int
    showTimes: List[ShowTimes]


class ShowTimesOut(ShowTimes):
    movies: List[Movie]


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    admin: Optional[bool] = False


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    admin: bool

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    admin: bool


class MovieShowTimeUpdate(BaseModel):
    movie_id: int
    showtime_id: int


class Booking(BaseModel):
    movieId: int
    movieName: str
    dateTime: str
    totalPrice: float
    emailAddress: EmailStr
    phoneNumber: str
    customerName: str
    adultNo: int
    studentNo: int
    childNo: int

    class Config:
        orm_mode = True


class BookingOut(Booking):
    id: int
    movie: MovieOut


class Comment(BaseModel):
    movieTitle: str
    customerName: str
    rating: int
    comment: str

    class Config:
        orm_mode = True


class CommentOut(Comment):
    id: int
