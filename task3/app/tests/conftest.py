import os
from dotenv import load_dotenv
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient


from app.database import Base
from app.main import app
from app.utils.users_crud import create_user
from app.models.users_models import UserCreate
from app.utils.auth import create_access_token
from app.models.blogs_models import BlogCreate
from app.utils.blogs_crud import create_blog

load_dotenv()

TEST_SQLALCHEMY_DATABASE_URL = os.getenv("TEST_SQLALCHEMY_DATABASE_URL")


@pytest.fixture(scope="session")
def db_session():
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def create_test_user(db_session):
    user_data = UserCreate(
        username="test_user",
        email="test@example.com",
        name="Test User",
        password="testpassword",
        role="user",
        bio="testbio",
        profile_picture="testprofile",
    )
    return create_user(db=db_session, user=user_data)


@pytest.fixture(scope="module")
def create_test_user_for_tag(db_session):
    user_data = UserCreate(
        username="test_user_for_tag",
        email="test_for_tag@example.com",
        name="Test User",
        password="testpassword",
        role="admin",
        bio="testbio",
        profile_picture="testprofile",
    )
    return create_user(db=db_session, user=user_data)


@pytest.fixture(scope="module")
def create_test_user_for_tag_not_admin(db_session):
    user_data = UserCreate(
        username="test_user_for_tag_not_admin",
        email="test_for_tag_not_admin@example.com",
        name="Test User",
        password="testpassword",
        role="user",
        bio="testbio",
        profile_picture="testprofile",
    )
    return create_user(db=db_session, user=user_data)


@pytest.fixture(scope="module")
def create_test_user_for_blog(db_session):
    user_data = UserCreate(
        username="test_user_for_blog",
        email="test_for_blog@example.com",
        name="Test User",
        password="testpassword",
        role="admin",
        bio="testbio",
        profile_picture="testprofile",
    )
    return create_user(db=db_session, user=user_data)


@pytest.fixture(scope="module")
def create_test_user_for_blog_not_owner(db_session):
    user_data = UserCreate(
        username="test_user_for_blog_not_owner",
        email="test_for_blog_not_owner@example.com",
        name="Test User",
        password="testpassword",
        role="admin",
        bio="testbio",
        profile_picture="testprofile",
    )
    return create_user(db=db_session, user=user_data)


@pytest.fixture(scope="module")
def current_user():
    return create_access_token(data={"sub": "test_user"})


@pytest.fixture(scope="module")
def current_user_for_tag():
    return create_access_token(data={"sub": "test_user_for_tag"})


@pytest.fixture(scope="module")
def current_user_for_tag_not_admin():
    return create_access_token(data={"sub": "test_user_for_tag_not_admin"})


@pytest.fixture(scope="module")
def current_user_for_blog():
    return create_access_token(data={"sub": "test_user_for_blog"})


@pytest.fixture(scope="module")
def current_user_for_blog_not_owner():
    return create_access_token(data={"sub": "test_user_for_blog_not_owner"})
