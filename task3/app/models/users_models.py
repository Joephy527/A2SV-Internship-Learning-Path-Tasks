from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str
    role: str


class UserCreate(UserBase):
    password: str
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class UserUpdate(BaseModel):
    username: str = Field(None)
    email: EmailStr = Field(None)
    password: str = Field(None)
    name: str = Field(None)
    bio: str = Field(None)
    profile_picture: str = Field(None)
    role: str = Field(None)

    class Config:
        orm_mode = True


class User(UserBase):
    password: str
    user_id: UUID
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
