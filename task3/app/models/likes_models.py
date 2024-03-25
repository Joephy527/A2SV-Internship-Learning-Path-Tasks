from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class Like(BaseModel):
    like_id: UUID
    user_id: UUID
    blog_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
