from fastapi import Depends, HTTPException, Response, status, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List


router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/")
def create_movie(
    movie: schemas.Movie,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    new_movie = models.Movie(**movie.dict())

    if current_user.admin != True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to perform this action because you are not an admin",
        )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return {new_movie}


@router.get("/{id}", response_model=List[schemas.MovieOut])
def get_movie(id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id).first()
    return {movie}


@router.delete("/{id}")
def delete_movie(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    movie_query = db.query(models.Movie).filter(models.Movie.id == id)

    if movie_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )

    if current_user.admin != True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to perform this action because you are not an admin",
        )
    movie_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/", response_model=List[schemas.MovieOut])
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(models.Movie).all()
    return movies
