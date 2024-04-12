from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


@dataclass(slots=True, kw_only=True)
class User:
    username: str
    email: str
    name: str
    role: str
    password: str
    user_id: UUID = field(default_factory=uuid4)
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime
