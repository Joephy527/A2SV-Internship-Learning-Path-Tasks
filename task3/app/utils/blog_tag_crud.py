from datetime import datetime
from sqlalchemy.orm import Session
from uuid import UUID

from app.models.blog_tags_models import BlogTagCreate, BlogTag, BlogTagUpdate
from app.schema import BlogTag


def get_blog_tags(db: Session, blog_id: UUID):
    return db.query(BlogTag).filter(BlogTag.blog_id == blog_id).all()


def get_blog_tags_by_tag(tag_name: str, db: Session):
    return db.query(BlogTag).filter(BlogTag.tag_name == tag_name).all()


def create_a_blog_tag(db: Session, blog_id: UUID, blog_tag_data: BlogTagCreate):
    created_at = datetime.now()
    updated_at = datetime.now()

    blog_tag = BlogTag(
        blog_id=blog_id,
        tag_name=blog_tag_data.tag_name,
        created_at=created_at,
        updated_at=updated_at,
    )

    db.add(blog_tag)
    db.commit()
    db.refresh(blog_tag)

    return blog_tag


def update_a_blog_tag(db: Session, blog_id: UUID, blog_tag_data: BlogTagUpdate):
    updated_at = datetime.now()

    blog_tag = (
        db.query(BlogTag)
        .filter(BlogTag.blog_id == blog_id, BlogTag.tag_name == blog_tag_data.tag_name)
        .first()
    )

    if blog_tag:
        blog_tag.tag_name = blog_tag_data.updated_tag_name
        blog_tag.updated_at = updated_at

        db.commit()
        db.refresh(blog_tag)

    return blog_tag


def delete_a_blog_tag(db: Session, blog_id: UUID, tag_name: str):
    blog_tag = (
        db.query(BlogTag)
        .filter(BlogTag.blog_id == blog_id, BlogTag.tag_name == tag_name)
        .first()
    )

    if blog_tag:
        db.delete(blog_tag)
        db.commit()

    return blog_tag
