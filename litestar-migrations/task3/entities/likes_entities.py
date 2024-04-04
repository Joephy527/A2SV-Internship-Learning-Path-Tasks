from datetime import datetime
from uuid import UUID

import msgspec


class Like(
    msgspec.Struct,
    forbid_unknown_fields=True,
):
    """A struct describing a like entity"""

    like_id: UUID
    user_id: UUID
    blog_id: UUID
    created_at: datetime
