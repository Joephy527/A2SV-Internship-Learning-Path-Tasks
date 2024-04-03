from datetime import datetime
from uuid import UUID

import msgspec


class BlogTagBase(
    msgspec.Struct,
    kw_only=True,
    tag_field="blog-tag",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    """A base struct for blog-tag entites"""

    tag_name: str


class BlogTagCreate(BlogTagBase):
    """A struct describing data for a blog-tag to be created"""

    pass


class BlogTagUpdate(BlogTagBase):
    """A struct describing update data for a blog-tag"""

    updated_tag_name: str


class BlogTag(BlogTagBase):
    """A struct describing a blog-tag entity"""

    blog_tag_id: UUID
    blog_id: UUID
    created_at: datetime
    updated_at: datetime
