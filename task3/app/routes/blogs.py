from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.middleware import get_current_user
from app.models.blogs_models import Blog, BlogCreate, BlogUpdate
from app.models.users_models import User
from app.utils import connect_db
from app.utils.blogs_crud import (
    create_blog,
    delete_blog,
    get_blog_by_id,
    get_blogs,
    update_blog,
)

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"],
)


# Route to get all blogs
@router.get("/")
def read_all_blogs(db: Session = Depends(connect_db)):
    return get_blogs(db)


# Route to get a blog by ID
@router.get("/{blog_id}")
def read_blog_by_id(blog_id: UUID, db: Session = Depends(connect_db)):
    db_blog = get_blog_by_id(db, blog_id)

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    return db_blog


# Route to create a new blog post
@router.post("/create", response_model=Blog)
def create_new_blog(
    blog: BlogCreate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    return create_blog(db=db, blog=blog, user_id=current_user.user_id)


# Route to update an existing blog
@router.put("/{blog_id}", response_model=Blog)
def update_existing_blog(
    blog_id: UUID,
    blog: BlogUpdate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    db_blog = update_blog(
        db=db, blog_id=blog_id, blog=blog, user_id=current_user.user_id
    )

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    return db_blog


# Route to delete an existing blog
@router.delete("/{blog_id}", response_model=Blog)
def delete_existing_blog(
    blog_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    db_blog = delete_blog(db=db, blog_id=blog_id, user_id=current_user.user_id)

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    return db_blog
