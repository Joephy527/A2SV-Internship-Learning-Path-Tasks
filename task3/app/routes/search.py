from fastapi import APIRouter, Depends, HTTPException, status
from schema import Blog
from sqlalchemy.orm import Session
from utils.blog_tag_crud import get_blog_tags_by_tag
from utils.blogs_crud import get_blog_by_title
from utils.users_crud import get_user_by_name, get_user_by_username
from utils import connect_db

router = APIRouter(
    prefix="/search",
    tags=["search"],
)


@router.get("/userName/{userName}")
async def get_user_with_userName(userName: str, db: Session = Depends(connect_db)):
    user = get_user_by_username(username=userName, db=db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


@router.get("/name/{name}")
async def get_user_with_name(name: str, db: Session = Depends(connect_db)):
    user = get_user_by_name(name=name, db=db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thier are no users with this name",
        )

    return user


@router.get("/blogTitle/{title}")
async def get_blog_with_title(title: str, db: Session = Depends(connect_db)):
    blog = get_blog_by_title(title=title, db=db)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thier are no blogs with this title",
        )

    return blog


@router.get("/blogTag/{tag}")
async def get_blog_with_tag(tag_name: str, db: Session = Depends(connect_db)):
    blogTags = get_blog_tags_by_tag(tag_name=tag_name, db=db)

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
