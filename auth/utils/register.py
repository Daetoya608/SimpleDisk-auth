from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc

from auth.db.models import User
from auth.schemas import RegistrationForm


async def register_user(session: AsyncSession, registration_form: RegistrationForm) -> tuple[bool, str]:
    new_user = User(**registration_form.model_dump())
    session.add(new_user)
    try:
        await session.commit()
    except exc.IntegrityError:
        return False, "Username already exists"
    return True, "Successful registration"
