from datetime import datetime
from uuid import UUID

import msgspec


class Follow(
    msgspec.Struct,
    forbid_unknown_fields=True,
):
    """A struct describing a follow entity"""

    Follow_id: UUID
    Follower_id: UUID
    Followed_user_id: UUID
    created_at: datetime
