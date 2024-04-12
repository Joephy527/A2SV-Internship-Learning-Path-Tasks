from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

import msgspec


class BlogBase(
    msgspec.Struct,
    kw_only=True,
    tag_field="blog",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    """A base struct for blog entites"""

    title: str
    content: str


class BlogCreate(BlogBase):
    """A struct describing data for a blog to be created"""

    pass


class BlogUpdate(
    msgspec.Struct, tag_field="blog", tag=str.lower, forbid_unknown_fields=True
):
    """A struct describing update data for a blog"""

    title: Optional[str] = None
    content: Optional[str] = None


@dataclass(slots=True)
class Blog(BlogBase):
    """A struct describing a blog entity"""

    blog_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
