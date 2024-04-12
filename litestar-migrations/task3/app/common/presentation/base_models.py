import msgspec


class UserBase(
    msgspec.Struct,
    kw_only=True,
    tag_field="blog",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    username: str
    email: str
    name: str
    role: str
