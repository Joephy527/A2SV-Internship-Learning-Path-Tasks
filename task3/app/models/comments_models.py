from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass

    class Config:
        orm_mode = True


class Comment(CommentBase):
    comment_id: UUID
    user_id: UUID
    blog_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
