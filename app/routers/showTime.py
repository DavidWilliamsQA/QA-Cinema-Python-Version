from fastapi import Depends, HTTPException, Response, status, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix="/showTime", tags=["ShowTimes"])


@router.post("/")
def create_showtime(
    time: schemas.ShowTimes,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    if current_user.admin == "true":
        new_time = models.ShowTime(**time.dict())
        db.add(new_time)
        db.commit()
        db.refresh(new_time)
        return new_time
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to perform this action because you are not an admin",
        )


@router.get("/")
def get_showtimes(db: Session = Depends(get_db)):
    movies = db.query(models.ShowTime).all()
    return movies


@router.delete("/{id}")
def delete_showTime(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    time_query = db.query(models.ShowTime).filter(models.ShowTime.id == id)

    if current_user.admin == "true":
        if time_query.first() == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"post with id: {id} does not exist",
            )
        time_query.delete(synchronize_session=False)
        db.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to perform this action because you are not an admin",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
