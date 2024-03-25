from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.rating_models import RatingCreate, RatingUpdate
from schema import BlogRating
from uuid import UUID


def get_ratings_by_blog_id(db: Session, blog_id: UUID):
    return db.query(BlogRating).filter(BlogRating.blog_id == blog_id).all()


def create_rating(db: Session, rating_data: RatingCreate, blog_id: UUID, user_id: UUID):
    created_at = datetime.now()
    updated_at = datetime.now()

    db_rating = BlogRating(
        rating=rating_data.rating,
        blog_id=blog_id,
        user_id=user_id,
        created_at=created_at,
        updated_at=updated_at,
    )

    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)

    return db_rating


def update_rating(db: Session, blog_id: UUID, rating_data: RatingUpdate, user_id: UUID):
    # Check if the user has already rated the blog
    db_rating = (
        db.query(BlogRating)
        .filter(BlogRating.blog_id == blog_id, BlogRating.user_id == user_id)
        .first()
    )

    # Update the rating
    if db_rating:
        if db_rating.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can not change other user's ratings",
            )

        db_rating.rating = rating_data.rating
        db_rating.updated_at = rating_data.updated_at

        db.commit()
        db.refresh(db_rating)

    return db_rating


def update_rating(db: Session, blog_id: UUID, rating_data: RatingUpdate, user_id: UUID):
    # Check if the user has already rated the blog
    db_rating = (
        db.query(BlogRating)
        .filter(BlogRating.blog_id == blog_id, BlogRating.user_id == user_id)
        .first()
    )

    # Update the rating
    if db_rating:
        if db_rating.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can not change other user's ratings",
            )

        db_rating.rating = rating_data.rating
        db_rating.updated_at = datetime.now()

        db.commit()
        db.refresh(db_rating)


def delete_rating(db: Session, blog_id: UUID, user_id: UUID):
    # Check if the user has already rated the blog
    db_rating = (
        db.query(BlogRating)
        .filter(BlogRating.blog_id == blog_id, BlogRating.user_id == user_id)
        .first()
    )

    # Delete the rating
    if db_rating:
        if db_rating.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can not delete other user's ratings",
            )

        db.delete(db_rating)
        db.commit()

    return db_rating
