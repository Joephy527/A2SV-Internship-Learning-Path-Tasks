from uuid import UUID
import msgspec

from typing import Optional, Annotated
from litestar import Litestar, get, post
from litestar.params import Body
from litestar.di import Provide
from sqlalchemy.orm import Session

from schemas import User, UserEntity, BlogEntity
from database import get_db_session


class UserBase(
    msgspec.Struct,
    kw_only=True,
    tag_field="blog",
    tag=str.lower,
    forbid_unknown_fields=True,
):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


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


@get(path="/", dependencies={"db": Provide(get_db_session)})
async def dsfwes(db: Session) -> str:
    ret = db.query(User).all()
    return ret if ret else "foisdjkf"


@post(path="/users", dependencies={"db": Provide(get_db_session)})
async def create_user(data: Annotated[UserCreate, Body()], db: Session) -> UserEntity:
    return UserEntity.create(user=data, db=db)


@post(path="/blogs/{user_id:uuid}", dependencies={"db": Provide(get_db_session)})
async def create_blog(
    data: Annotated[BlogCreate, Body()], user_id: UUID, db: Session
) -> BlogEntity:
    blog_instance = BlogEntity()
    return blog_instance.create(blog=data, user_id=user_id, db=db)


app = Litestar([dsfwes, create_user, create_blog])
