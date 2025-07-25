from passlib.exc import UnknownHashError

from auth.config import get_settings


def hash_password(password: str) -> str:
    settings = get_settings()
    password = settings.PWD_CONTEXT.hash(password)
    return password


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    pwd_context = get_settings().PWD_CONTEXT
    try:  # ERROR: Приложение падало при попытке передать пароль захешированный с помощью другой функции
        return pwd_context.verify(plain_password, hashed_password)
    except UnknownHashError:
        return False
