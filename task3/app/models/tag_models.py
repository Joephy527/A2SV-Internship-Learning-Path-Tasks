from datetime import datetime
from pydantic import BaseModel


class TagBase(BaseModel):
    tag_name: str


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    update_tag_name: str


class Tag(TagBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
