from datetime import datetime
from uuid import UUID

import msgspec


class CommentBase(
    msgspec.Struct,
    kw_only=True,
    tag_field="comment",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    """A base struct for comment entites"""

    content: str


class CommentCreate(CommentBase):
    """A struct describing data for a comment to be created"""

    pass


class CommentUpdate(CommentBase):
    """A struct describing update data for a comment"""

    pass


class Comment(CommentBase):
    """A struct describing a comment entity"""

    comment_id: UUID
    user_id: UUID
    blog_id: UUID
    created_at: datetime
    updated_at: datetime
