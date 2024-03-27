from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.schema import Follower


def follow(db: Session, follower_id: UUID, followed_id: UUID):
    created_at = datetime.now()

    follow = (
        db.query(Follower)
        .filter(
            Follower.follower_id == follower_id,
            Follower.followed_user_id == followed_id,
        )
        .first()
    )
    new_follow = None

    if not follow:
        new_follow = Follower(
            followed_user_id=followed_id, follower_id=follower_id, created_at=created_at
        )

        db.add(new_follow)
        db.commit()
        db.refresh(new_follow)

    return new_follow


def unfollow(db: Session, follow_id: UUID, user_id: UUID):
    follow = db.query(Follower).filter(Follower.follow_id == follow_id).first()

    if follow:
        if follow.follower_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can not unfollow other user's follow list",
            )

        db.delete(follow)
        db.commit()

    return follow
