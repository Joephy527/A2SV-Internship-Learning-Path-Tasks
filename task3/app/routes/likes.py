from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.middleware import get_current_user
from app.models.users_models import User
from app.schema import Blog
from app.utils.likes_crud import like, unlike
from app.utils import connect_db

router = APIRouter(
    prefix="/likes",
    tags=["likes"],
)


@router.post("/{blog_id}/create")
def create_like(
    blog_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    db_blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    new_like = like(db=db, user_id=current_user.user_id, blog_id=blog_id)

    if not new_like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already liked the blog",
        )

    return new_like


@router.delete("/{like_id}")
def delete_like(
    like_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    deleted_like = unlike(db=db, like_id=like_id, user_id=current_user.user_id)

    if not deleted_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="You Haven't liked the blog"
        )

    return deleted_like
