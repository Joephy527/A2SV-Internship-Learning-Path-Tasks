from passlib.context import CryptContext

from database import SessionLocal

def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create an instance of CryptContext with appropriate hashing algorithms and settings
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a password using CryptContext.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if a plain password matches a hashed password.
    
    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password.
    
    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)
