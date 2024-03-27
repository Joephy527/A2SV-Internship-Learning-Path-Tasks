from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.middleware import get_current_user
from app.models.users_models import User
from app.models.rating_models import RatingCreate, RatingUpdate, Rating
from app.schema import BlogRating
from app.utils.rating_crud import create_rating, update_rating, delete_rating
from app.utils import connect_db

router = APIRouter(
    prefix="/ratings",
    tags=["rating"],
)


@router.post("/{blog_id}/", response_model=Rating)
def create_rating_for_blog(
    blog_id: UUID,
    rating_data: RatingCreate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    db_rating = (
        db.query(BlogRating)
        .filter(
            BlogRating.blog_id == blog_id, BlogRating.user_id == current_user.user_id
        )
        .first()
    )

    if db_rating:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You've already rated this blogm try updating your rating",
        )

    rating = create_rating(
        db=db, rating_data=rating_data, blog_id=blog_id, user_id=current_user.user_id
    )

    return rating


@router.put("/{blog_id}/", response_model=Rating)
def update_rating_for_blog(
    blog_id: UUID,
    rating_data: RatingUpdate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    # Assuming there's only one rating per user for a specific blog
    rating = update_rating(
        db=db, blog_id=blog_id, rating_data=rating_data, user_id=current_user.user_id
    )

    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rating not found for the specified blog",
        )

    return rating


@router.delete("/{blog_id}/", response_model=Rating)
def delete_rating_for_blog(
    blog_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    # Assuming there's only one rating per user for a specific blog
    rating = delete_rating(db=db, blog_id=blog_id, user_id=current_user.user_id)

    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rating not found for the specified blog",
        )

    return rating
