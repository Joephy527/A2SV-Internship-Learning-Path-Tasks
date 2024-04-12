from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, registry, Session

from database import Base, engine


@dataclass(slots=True, kw_only=True)
class UserEntity:
    user_id: UUID = field(default_factory=uuid4)
    username: str
    email: str
    password: str

    @classmethod
    def create(cls, user, db: Session):
        new_user = cls(username=user.username, email=user.email, password=user.password)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user


@dataclass(slots=True, kw_only=True)
class BlogEntity:
    blog_id: UUID = field(default_factory=uuid4)
    user_id: UUID = field(default_factory=uuid4)
    title: str
    content: str

    @classmethod
    def create(cls, blog, user_id, db: Session):
        created_at = datetime.now()
        updated_at = datetime.now()

        db_blog = cls(
            title=blog.title,
            content=blog.content,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)

        return db_blog


class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="user")


class Blog(Base):
    __tablename__ = "blogs"
    blog_id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE")
    )
    title = Column(String)
    content = Column(String)

    user = relationship("User", back_populates="blogs", cascade="all, delete-orphan")


mapper_registry = registry()
mapper = mapper_registry.map_imperatively


def start_mappers():
    mapper(UserEntity, User)
    mapper(BlogEntity, Blog)


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    start_mappers()
    create_tables()
