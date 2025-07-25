from sqlalchemy import delete, exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.db.models import User
from auth.schemas import RegistrationForm
from auth.utils.base import verify_password, get_user


async def authenticate_user(
    session: AsyncSession,
    username: str,
    password: str,
) -> User | bool:
    user = await get_user(session, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
