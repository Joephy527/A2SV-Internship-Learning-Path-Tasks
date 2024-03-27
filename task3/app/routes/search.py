from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schema import Blog, BlogTag, User
from app.utils import connect_db

router = APIRouter(
    prefix="/search",
    tags=["search"],
)


@router.get("/userName/{user_name}")
async def get_user_with_userName(user_name: str, db: Session = Depends(connect_db)):
    user = db.query(User).filter(User.username.like(f"%{user_name}%")).all()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


@router.get("/name/{name}")
async def get_user_with_name(name: str, db: Session = Depends(connect_db)):
    user = db.query(User).filter(User.name.like(f"%{name}%")).all()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thier are no users with this name",
        )

    return user


@router.get("/blogTitle/{title}")
async def get_blog_with_title(title: str, db: Session = Depends(connect_db)):
    blog = db.query(Blog).filter(Blog.title.like(f"%{title}%")).all()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thier are no blogs with this title",
        )

    return blog


@router.get("/blogTag/{tag}")
async def get_blog_with_tag(tag_name: str, db: Session = Depends(connect_db)):
    blogTags = db.query(BlogTag).filter(BlogTag.tag_name.like(f"%{tag_name}%")).all()

    if not blogTags:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blogs with this tag not found",
        )

    blogs = []

    for row in blogTags:
        blog = db.query(Blog).filter(Blog.blog_id == row.blog_id).first()
        blogs.append(blog)

    return blogs
