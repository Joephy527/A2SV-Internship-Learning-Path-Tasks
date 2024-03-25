from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class Follow(BaseModel):
    Follow_id: UUID
    Follower_id: UUID
    Followed_user_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
