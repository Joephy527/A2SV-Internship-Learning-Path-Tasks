from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RatingBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    rating: Optional[int] = None


class Rating(RatingBase):
    rating_id: UUID
    blog_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
