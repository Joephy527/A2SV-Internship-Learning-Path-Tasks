from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import SEQLALCHEMY_DATABASE_URL

# DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SEQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
