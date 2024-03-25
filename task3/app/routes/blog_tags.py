from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

import schema
from middleware import get_current_user
from models.bolg_tags_models import BlogTagBase, BlogTagCreate, BlogTag, BlogTagUpdate
from models.users_models import User
from schema import Blog
from sqlalchemy.orm import Session
from utils import connect_db
from utils.tags_crud import get_tag_by_tag_name
from utils.blog_tag_crud import create_a_blog_tag, get_blog_tags, update_a_blog_tag, delete_a_blog_tag

router = APIRouter(
    prefix="/blog_tags/{blog_id}",
    tags=["blog tags"],
)

@router.get("/", response_model=list[BlogTag])
async def get_all_blog_tags(blog_id: UUID, db: Session = Depends(connect_db)):
    return get_blog_tags(db=db, blog_id=blog_id)

@router.post("/", response_model=BlogTag)
async def create_blog_tag(blog_id: UUID, blog_tag_data: BlogTagCreate, db: Session = Depends(connect_db), current_user: User = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()
    db_blog_tag = db.query(schema.BlogTag).filter(schema.BlogTag.blog_id == blog_id, schema.BlogTag.tag_name == blog_tag_data.tag_name).first()
    
    if db_blog_tag:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tag has already been added fot this blog")
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    # Assign the user ID associated with the blog
    user_id = blog.user_id
    
    # Check if the current user is the owner of the blog
    if user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only the owner of the blog can create blog tags")
    
    return create_a_blog_tag(db=db, blog_tag_data=blog_tag_data, blog_id=blog_id)

@router.put("/", response_model=BlogTag)
async def update_blog_tag(blog_id: UUID, blog_tag_data: BlogTagUpdate, db: Session = Depends(connect_db), current_user: User = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()
    db_tag = get_tag_by_tag_name(db=db, tag_name=blog_tag_data.tag_name)
    db_updated_tag_name = get_tag_by_tag_name(db=db, tag_name=blog_tag_data.updated_tag_name) 
    
    if not db_tag or not db_updated_tag_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{blog_tag_data.tag_name} or {blog_tag_data.updated_tag_name} is not a valid tag")
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    # Assign the user ID associated with the blog
    user_id = blog.user_id
    
    # Check if the current user is the owner of the blog
    if user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only the owner of the blog can update blog tags")
    
    updated_blog_tag = update_a_blog_tag(db=db, blog_id=blog_id, blog_tag_data=blog_tag_data)
    
    if not updated_blog_tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The blog doesn't have this tag")
    
    return updated_blog_tag

@router.delete("/", response_model=BlogTag)
async def delete_blog_tag(blog_id: UUID, tag_data: BlogTagBase, db: Session = Depends(connect_db), current_user: User = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    # Assign the user ID associated with the blog
    user_id = blog.user_id
    
    # Check if the current user is the owner of the blog
    if user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only the owner of the blog can delete blog tags")
    
    deleted_blog_tag = delete_a_blog_tag(db=db, blog_id=blog_id, tag_name=tag_data.tag_name)

    if not deleted_blog_tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The blog doesn't have this tag")
    
    return deleted_blog_tag