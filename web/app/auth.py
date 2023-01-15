from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist

from app.models import User

security = HTTPBasic()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    def raise_exception():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={'WWW-Authenticate': 'Basic'},
        )

    try:
        user = await User.get(username=credentials.username)
    except DoesNotExist:
        raise_exception()

    if not verify_password(credentials.password, user.password):
        raise_exception()

    return user
