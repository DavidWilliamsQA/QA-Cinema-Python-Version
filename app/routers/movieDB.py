from fastapi import APIRouter
import requests

# from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
import os
from dotenv import load_dotenv

load_dotenv()


router = APIRouter(prefix="/dbMovies", tags=["DBMovies"])


@router.get("/{id}")
def get_movie(id: int):
    res = requests.get(
        f"https://api.themoviedb.org/3/movie/{id}?api_key={os.getenv('MOVIE_DB_API_KEY')}&language=en-UK"
    )
    print(res.json())
    return res.json()
