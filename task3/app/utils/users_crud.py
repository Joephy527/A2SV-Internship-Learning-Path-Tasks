from datetime import datetime
from sqlalchemy.orm import Session
from uuid import UUID

from models.users_models import UserCreate, UserUpdate
from schema import User
from utils import hash_password


def get_user_by_id(db: Session, user_id: UUID):
    return db.query(User).filter(User.user_id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def create_user(user: UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    created_at = datetime.now()
    updated_at = datetime.now()

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        name=user.name,
        bio=user.bio,
        profile_picture=user.profile_picture,
        role=user.role,
        created_at=created_at,
        updated_at=updated_at,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Update existing user
def update_user(db: Session, user_id: UUID, user: UserUpdate):
    db_user = db.query(User).filter(User.user_id == user_id).first()

    if db_user:
        update_data = user.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            if value:
                if key == "password":
                    value = hash_password(value)

                setattr(db_user, key, value)

        db_user.updated_at = datetime.now()

        db.commit()
        db.refresh(db_user)

    return db_user


# Delete existing user
def delete_user(db: Session, user_id: UUID):
    db_user = db.query(User).filter(User.user_id == user_id).first()

    db.delete(db_user)
    db.commit()

    return db_user
