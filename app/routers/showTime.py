from fastapi import Depends, HTTPException, Response, status, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix="/showTime", tags=["ShowTimes"])


@router.post("/")
def create_time(
    time: schemas.ShowTimes,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    admin_status = current_user.admin
    print(admin_status)
    if admin_status == "true":
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
def get_times(db: Session = Depends(get_db)):
    movies = db.query(models.ShowTime).all()
    return movies


@router.delete("/{id}")
def delete_showTime(id: int, db: Session = Depends(get_db)):
    time_query = db.query(models.ShowTime).filter(models.ShowTime.id == id)

    if time_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    time_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
