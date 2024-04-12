from typing import Optional
from uuid import UUID

import msgspec

from common.presentation.base_models import UserBase


class UserCreate(UserBase):
    password: str
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class UserUpdate(
    msgspec.Struct,
    kw_only=True,
    tag_field="blog",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    role: Optional[str] = None
