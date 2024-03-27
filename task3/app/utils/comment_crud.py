from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.models.comments_models import CommentCreate, CommentUpdate
from app.schema import Comment


def create_comment(db: Session, user_id: UUID, blog_id: UUID, comment: CommentCreate):
    created_at = datetime.now()
    updated_at = datetime.now()

    new_comment = Comment(
        content=comment.content,
        user_id=user_id,
        blog_id=blog_id,
        created_at=created_at,
        updated_at=updated_at,
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


def edit_comment(db: Session, comment_id: UUID, user_id: UUID, comment: CommentUpdate):
    updated_at = datetime.now()

    db_comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()

    if db_comment:
        if db_comment.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can not edit other users comments",
            )

        updated_comment = comment.model_dump(exclude_unset=True)

        for key, value in updated_comment.items():
            if value:
                setattr(db_comment, key, value)

        db_comment.updated_at = updated_at
        db.commit()
        db.refresh(db_comment)

    return db_comment


def delete_comment(db: Session, comment_id: UUID, user_id: UUID):
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()

    if comment:
        if comment.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can not delete other users comments",
            )

        db.delete(comment)
        db.commit()

    return comment
