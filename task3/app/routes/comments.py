from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.middleware import get_current_user
from app.models.users_models import User
from app.models.comments_models import CommentCreate, CommentUpdate
from app.utils.comment_crud import create_comment, edit_comment, delete_comment
from app.utils import connect_db

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
)


@router.post("/{blog_id}/create")
def create_blog_comment(
    blog_id: UUID,
    comment: CommentCreate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    return create_comment(
        db=db, user_id=current_user.user_id, blog_id=blog_id, comment=comment
    )


@router.put("/{comment_id}")
def edit_blog_comment(
    comment_id: UUID,
    comment: CommentUpdate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    edited_comment = edit_comment(
        db=db, comment_id=comment_id, user_id=current_user.user_id, comment=comment
    )

    if not edited_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )

    return edited_comment


@router.delete("/{comment_id}")
def delete_blog_comment(
    comment_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    deleted_comment = delete_comment(
        db=db, comment_id=comment_id, user_id=current_user.user_id
    )

    if not deleted_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )

    return deleted_comment
