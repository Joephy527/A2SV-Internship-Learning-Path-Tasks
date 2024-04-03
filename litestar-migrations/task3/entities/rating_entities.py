from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID

import msgspec


class RatingBase(
    msgspec.Struct,
    kw_only=True,
    tag_field="rating",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    """A base struct for rating entites"""

    rating: Annotated[int, msgspec.Meta(ge=1, le=5)]


class RatingCreate(RatingBase):
    """A struct describing data for a rating to be created"""

    pass


class RatingUpdate(
    msgspec.Struct,
    kw_only=True,
    tag_field="rating",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    """A struct describing update data for a rating"""

    rating: Annotated[Optional[int], msgspec.Meta(ge=1, le=5)]


class Rating(RatingBase):
    """A struct describing a rating entity"""

    rating_id: UUID
    blog_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
