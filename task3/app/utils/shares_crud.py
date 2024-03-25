from datetime import datetime
from schema import Share
from sqlalchemy.orm import Session
from uuid import UUID


def share(db: Session, user_id: UUID, blog_id: UUID):
    created_at = datetime.now()

    new_share = Share(user_id=user_id, blog_id=blog_id, created_at=created_at)

    db.add(new_share)
    db.commit()
    db.refresh(new_share)

    return new_share
