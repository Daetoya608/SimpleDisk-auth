from pydantic import BaseModel, validator, EmailStr

from auth.config import get_settings
from auth.utils.base import hash_password


class RegistrationForm(BaseModel):
    username: str
    password: str
    email: EmailStr

    @validator("password")
    def hash_password_val(cls, password):
        return hash_password(password)


class RegistrationSuccess(BaseModel):
    message: str
    status: int
