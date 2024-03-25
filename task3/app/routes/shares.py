from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from middleware import get_current_user
from models.users_models import User
from models.shares_models import ShareCreate
from utils import connect_db
from utils.shares_crud import share

router = APIRouter(
    prefix="/shares",
    tags=["shares"],
)


@router.post("/{blog_id}/create")
def create_like(
    blog_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    return share(db=db, user_id=current_user.user_id, blog_id=blog_id)
