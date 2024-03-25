from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class BlogTagBase(BaseModel):
    tag_name: str


class BlogTagCreate(BlogTagBase):
    pass


class BlogTagUpdate(BlogTagBase):
    updated_tag_name: str

    class Config:
        orm_mode = True


class BlogTag(BlogTagBase):
    blog_tag_id: UUID
    blog_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
