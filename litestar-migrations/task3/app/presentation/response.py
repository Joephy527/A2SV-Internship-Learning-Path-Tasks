from datetime import datetime
from typing import Optional
from uuid import UUID

from common.presentation.base_models import UserBase


class User(UserBase):
    password: str
    user_id: UUID
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    created_at: datetime
    updated_at: datetime
