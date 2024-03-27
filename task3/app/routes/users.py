from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.middleware import get_current_user
from app.models.token_models import TokenData
from app.models.users_models import User, UserCreate, UserUpdate
from app.utils import connect_db
from app.utils.users_crud import (
    create_user,
    delete_user,
    get_user_by_id,
    get_user_by_username,
    update_user,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me")
async def read_users_me(current_user: TokenData = Depends(get_current_user)):
    return current_user


@router.get("/{user_id}", response_model=User)
def read_user(user_id: UUID, db: Session = Depends(connect_db)):
    db_user = get_user_by_id(db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return db_user


@router.post("/create", response_model=User)
def create_users(user: UserCreate, db: Session = Depends(connect_db)):
    existing_user = get_user_by_username(username=user.username, db=db)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    return create_user(user=user, db=db)


# Update User
@router.put("/{user_id}", response_model=User)
def update_existing_user(
    user_id: UUID,
    user: UserUpdate,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You Can't Change Other User's Profiles",
        )

    db_user = update_user(db=db, user_id=user_id, user=user)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return db_user


# Delete User
@router.delete("/{user_id}", response_model=User)
def delete_existing_user(
    user_id: UUID,
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You Can't Delete Other User's Profiles",
        )

    db_user = delete_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return db_user
