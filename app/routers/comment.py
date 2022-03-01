from fastapi import Depends, HTTPException, status, APIRouter, Response
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/", response_model=schemas.Comment)
def create_comment(comment: schemas.Comment, db: Session = Depends(get_db)):

    return


@router.get("/{id}", response_model=schemas.Comment)
def get_comment(id: int, db: Session = Depends(get_db)):

    return


@router.delete("/{id}")
def delete_comment(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    comment_query = db.query(models.Comment).filter(models.Comment.id == id)

    if comment_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment with id: {id} does not exist",
        )

    if current_user.admin != "true":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to perform this action because you are not an admin",
        )

    comment_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/", response_model=List[schemas.Comment])
def get_comments(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    if current_user.admin != "true":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to perform this action because you are not an admin",
        )
    comments = db.query(models.Comment).all()
    return comments
