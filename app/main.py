from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import movie, user, auth, showTime, time, booking

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(movie.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(showTime.router)
app.include_router(time.router)
app.include_router(booking.router)
