from fastapi import Depends, HTTPException, Response, status, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/time", tags=["Time"])

# Deletes a specific show time from a specific Movie
@router.delete("/deleteTime")
def delete_time(
    update: schemas.MovieShowTimeUpdate,
    db: Session = Depends(get_db),
):
    time_query = (
        db.query(models.MovieShowTimes)
        .filter(models.MovieShowTimes.showtime_id == update.showtime_id)
        .filter(models.MovieShowTimes.movie_id == update.movie_id)
    )

    if time_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"time does not exist",
        )
    print(time_query.delete(synchronize_session=False))
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Adds a specific showtime to a specific movie
@router.post("/createTime")
def set_showTime_to_movie(
    update: schemas.MovieShowTimeUpdate,
    db: Session = Depends(get_db),
):
    new_movie_showTime = models.MovieShowTimes(**update.dict())

    db.add(new_movie_showTime)
    db.commit()
    db.refresh(new_movie_showTime)

    return new_movie_showTime
