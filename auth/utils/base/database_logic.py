from sqlalchemy import delete, exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.db.models import User
from auth.schemas import RegistrationForm


async def get_user(session: AsyncSession, username: str) -> User | None:
    query = select(User).where(User.username == username)
    return await session.scalar(query)


async def delete_user(session: AsyncSession, user: User) -> None:
    query = delete(User).where(User.username == user.username)
    await session.execute(query)
    await session.commit()
