from datetime import datetime
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session, load_only
from schema import Blog, BlogRating, BlogTag, Comment, Like, Share
from models.blogs_models import BlogCreate, BlogUpdate


# Get all blogs
def get_blogs(db: Session):
    blogs_with_tags_and_ratings = (
        db.query(Blog, BlogTag, BlogRating)
        .outerjoin(BlogTag, Blog.blog_id == BlogTag.blog_id)
        .outerjoin(BlogRating, Blog.blog_id == BlogRating.blog_id)
        .all()
    )

    combined_data = {}

    for blog, blog_tag, rating in blogs_with_tags_and_ratings:
        if blog.blog_id not in combined_data:
            combined_data[blog.blog_id] = {
                "blog_id": blog.blog_id,
                "user_id": blog.user_id,
                "title": blog.title,
                "content": blog.content,
                "created_at": blog.created_at,
                "updated_at": blog.updated_at,
                "tags": set(),
                "ratings": set(),
            }

        if blog_tag:
            combined_data[blog.blog_id]["tags"].add(blog_tag)

        if rating:
            combined_data[blog.blog_id]["ratings"].add(rating)

    return list(combined_data.values())


# Get blog by ID
def get_blog_by_id(db: Session, blog_id: UUID):
    blog_data = (
        db.query(Blog, BlogTag, BlogRating, Like, Share, Comment)
        .outerjoin(BlogTag, Blog.blog_id == BlogTag.blog_id)
        .outerjoin(BlogRating, Blog.blog_id == BlogRating.blog_id)
        .outerjoin(Like, Blog.blog_id == Like.blog_id)
        .outerjoin(Share, Blog.blog_id == Share.blog_id)
        .outerjoin(Comment, Blog.blog_id == Comment.blog_id)
        .filter(Blog.blog_id == blog_id)
        .all()
    )

    if not blog_data:
        return None

    combined_data = {}

    for blog, blog_tag, blog_rating, like, share, comment in blog_data:
        if blog.blog_id not in combined_data:
            combined_data[blog.blog_id] = {
                "blog_id": blog.blog_id,
                "user_id": blog.user_id,
                "title": blog.title,
                "content": blog.content,
                "created_at": blog.created_at,
                "updated_at": blog.updated_at,
                "tags": set(),
                "ratings": set(),
                "likes": set(),
                "shares": set(),
                "comments": set(),
            }

        if blog_tag:
            combined_data[blog.blog_id]["tags"].add(blog_tag)

        if blog_rating:
            combined_data[blog.blog_id]["ratings"].add(blog_rating)

        if like:
            combined_data[blog.blog_id]["likes"].add(like)

        if share:
            combined_data[blog.blog_id]["shares"].add(share)

        if comment:
            combined_data[blog.blog_id]["comments"].add(comment)

    return list(combined_data.values())


def get_blog_by_title(title: str, db: Session):
    return db.query(Blog).filter(Blog.title == title).all()


# Create new blog
def create_blog(db: Session, blog: BlogCreate, user_id: UUID):
    created_at = datetime.now()
    updated_at = datetime.now()

    db_blog = Blog(
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


# Update existing blog
def update_blog(db: Session, blog_id: UUID, blog: BlogUpdate, user_id: UUID):
    updated_at = datetime.now()

    db_blog = (
        db.query(Blog)
        .options(load_only(Blog.created_at))
        .filter(Blog.blog_id == blog_id)
        .first()
    )

    if db_blog:
        if db_blog.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not the Owner of The Blog",
            )

        updated_blog = blog.model_dump(exclude_unset=True)

        for key, value in updated_blog.items():
            setattr(db_blog, key, value)

        db_blog.updated_at = updated_at
        db.commit()
        db.refresh(db_blog)

    return db_blog


# Delete existing blog
def delete_blog(db: Session, blog_id: UUID, user_id: UUID):
    db_blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()

    if db_blog:
        if db_blog.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not the Owner of The Blog",
            )

        db.delete(db_blog)
        db.commit()

    return db_blog
