import uuid
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    bio = Column(String)
    profile_picture = Column(String)  # Assuming the profile picture is stored as a URL
    role = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    blogs = relationship("Blog", back_populates="user")
    blog_ratings = relationship("BlogRating", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")
    shares = relationship("Share", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    followers = relationship(
        "Follower", back_populates="follower", foreign_keys="Follower.follower_id"
    )
    following = relationship(
        "Follower",
        back_populates="followed_user",
        foreign_keys="Follower.followed_user_id",
    )


class Blog(Base):
    __tablename__ = "blogs"
    blog_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="blogs")
    ratings = relationship("BlogRating", back_populates="blog")
    tags = relationship("BlogTag", back_populates="blog")
    comments = relationship("Comment", back_populates="blog")
    likes = relationship("Like", back_populates="blog")
    shares = relationship("Share", back_populates="blog")


class BlogRating(Base):
    __tablename__ = "blog_ratings"
    rating_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    blog_id = Column(UUID(as_uuid=True), ForeignKey("blogs.blog_id"))
    rating = Column(Integer)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="blog_ratings")
    blog = relationship("Blog", back_populates="ratings")


class Tag(Base):
    __tablename__ = "tags"
    tag_name = Column(String, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    blogs = relationship("BlogTag", back_populates="tag")


class BlogTag(Base):
    __tablename__ = "blog_tags"
    blog_tag_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    blog_id = Column(UUID(as_uuid=True), ForeignKey("blogs.blog_id"))
    tag_name = Column(String, ForeignKey("tags.tag_name"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    blog = relationship("Blog", back_populates="tags")
    tag = relationship("Tag", back_populates="blogs")


class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    blog_id = Column(UUID(as_uuid=True), ForeignKey("blogs.blog_id"))
    content = Column(String)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="comments")
    blog = relationship("Blog", back_populates="comments")


class Like(Base):
    __tablename__ = "likes"
    like_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    blog_id = Column(UUID(as_uuid=True), ForeignKey("blogs.blog_id"))
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="likes")
    blog = relationship("Blog", back_populates="likes")


class Share(Base):
    __tablename__ = "shares"
    share_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    blog_id = Column(UUID(as_uuid=True), ForeignKey("blogs.blog_id"))
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="shares")
    blog = relationship("Blog", back_populates="shares")


class Notification(Base):
    __tablename__ = "notifications"
    notification_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    content = Column(String)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="notifications")


class Follower(Base):
    __tablename__ = "followers"
    follow_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    follower_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    followed_user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    created_at = Column(DateTime, nullable=False)

    follower = relationship(
        "User", foreign_keys=[follower_id], back_populates="followers"
    )
    followed_user = relationship(
        "User", foreign_keys=[followed_user_id], back_populates="following"
    )


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
