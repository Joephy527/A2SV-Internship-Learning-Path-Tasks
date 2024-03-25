from datetime import datetime
from schema import Like
from sqlalchemy.orm import Session
from uuid import UUID


def like(db: Session, user_id: UUID, blog_id: UUID):
    created_at = datetime.now()

    like = (
        db.query(Like).filter(Like.blog_id == blog_id, Like.user_id == user_id).first()
    )
    new_like = None

    if not like:
        new_like = Like(user_id=user_id, blog_id=blog_id, created_at=created_at)

        db.add(new_like)
        db.commit()
        db.refresh(new_like)

    return new_like


def unlike(db: Session, like_id: UUID, user_id: UUID):
    like = (
        db.query(Like).filter(Like.like_id == like_id, Like.user_id == user_id).first()
    )

    if like:
        db.delete(like)
        db.commit()

    return like
