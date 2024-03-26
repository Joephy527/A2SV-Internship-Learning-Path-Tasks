from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from middleware import get_current_user_role
from models.tag_models import TagCreate, TagUpdate, Tag
from utils import connect_db
from utils.tags_crud import (
    create_a_tag,
    delete_existing_tag,
    edit_tag,
    get_tag_by_tag_name,
    get_tags,
)

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
)


@router.get("/", response_model=list[Tag])
async def get_all_tags(db: Session = Depends(connect_db)):
    return get_tags(db=db)


@router.post("/", response_model=Tag)
async def create_tag(
    tag_data: TagCreate,
    db: Session = Depends(connect_db),
    user_role: str = Depends(get_current_user_role),
):
    if user_role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Only Admins Can Create a Tag"
        )

    existing_tag = get_tag_by_tag_name(tag_name=tag_data.tag_name, db=db)

    if existing_tag:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tag already Exists"
        )

    return create_a_tag(db=db, tag_data=tag_data)


@router.put("/{tag_name}", response_model=Tag)
async def update_tag(
    tag_name: str,
    tag_data: TagUpdate,
    db: Session = Depends(connect_db),
    user_role: str = Depends(get_current_user_role),
):
    if user_role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Only Admins Can Update a Tag"
        )

    updated_tag = edit_tag(db=db, tag_name=tag_name, tag_data=tag_data)

    if not updated_tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not Found"
        )

    return updated_tag


@router.delete("/{tag_name}/")
async def delete_tag(
    tag_name: str,
    db: Session = Depends(connect_db),
    user_role: str = Depends(get_current_user_role),
):
    if user_role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Only Admins Can Delete a Tag"
        )

    deleted_tag = delete_existing_tag(db=db, tag_name=tag_name)

    if not deleted_tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not Found"
        )

    return deleted_tag
