from datetime import datetime
from sqlalchemy.orm import Session
from schema import Tag
from models.tag_models import TagCreate, TagUpdate


def get_tag_by_tag_name(tag_name: str, db: Session):
    tag_name = db.query(Tag).filter(Tag.tag_name == tag_name).first()

    return tag_name


def create_a_tag(db: Session, tag_data: TagCreate):
    db_tag = Tag(**tag_data.model_dump())

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)

    return db_tag


def create_a_tag(db: Session, tag_data: TagCreate):
    created_at = datetime.now()
    updated_at = datetime.now()

    db_tag = Tag(
        tag_name=tag_data.tag_name, created_at=created_at, updated_at=updated_at
    )

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)

    return db_tag


def edit_tag(db: Session, tag_name: str, tag_data: TagUpdate):
    db_tag = get_tag_by_tag_name(db=db, tag_name=tag_name)

    if db_tag:
        db_tag.tag_name = tag_data.update_tag_name
        db_tag.updated_at = datetime.now()
        db.commit()
        db.refresh(db_tag)

    return db_tag


def delete_existing_tag(db: Session, tag_name: str):
    db_tag = get_tag_by_tag_name(db=db, tag_name=tag_name)

    if db_tag:
        db.delete(db_tag)
        db.commit()

    return db_tag


def get_tags(db: Session):
    return db.query(Tag).all()
