import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
TEST_SQLALCHEMY_DATABASE_URL = os.getenv("TEST_SQLALCHEMY_DATABASE_URL")
ENVIRONMENT = os.getenv("ENVIRONMENT")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def set_database_url(env):
    if env == "dev":
        return DATABASE_URL
    elif env == "test":
        return TEST_SQLALCHEMY_DATABASE_URL
    else:
        raise ValueError(f"Invalid environment: {env}")


SEQLALCHEMY_DATABASE_URL = set_database_url(ENVIRONMENT)
