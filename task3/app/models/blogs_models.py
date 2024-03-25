from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID


class BlogBase(BaseModel):
    title: str
    content: str


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BaseModel):
    title: str = Field(None)
    content: str = Field(None)

    class Config:
        orm_mode = True


class Blog(BlogBase):
    blog_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
