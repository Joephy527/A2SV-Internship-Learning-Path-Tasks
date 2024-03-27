from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

import app.schema as schema
from app.middleware import get_current_user
from app.models.users_models import User
from app.utils import connect_db
from app.utils.followers_crud import follow, unfollow

router = APIRouter(
    prefix="/follow",
    tags=["follow"],
)


@router.post("/{user_id}/create")
def create_follow(
    user_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    db_user = db.query(schema.User).filter(schema.User.user_id == user_id).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )

    new_follow = follow(db=db, follower_id=current_user.user_id, followed_id=user_id)

    if not new_follow:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already followed the user",
        )

    return new_follow


@router.delete("/{follow_id}")
def delete_follow(
    follow_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    deleted_like = unfollow(db=db, follow_id=follow_id, user_id=current_user.user_id)

    if not deleted_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="You Haven't liked the blog"
        )

    return deleted_like
