from sqlalchemy import Column, String, Text, TIMESTAMP, BOOLEAN
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from auth.db import DeclarativeBase


class RefreshToken(DeclarativeBase):
    __tablename__ = "refresh_token"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        unique=True,
        doc="Unique ID"
    )
    user_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
        doc="relation with user"
    )
    refresh_token = Column(
        Text,
        nullable=False,
        unique=True,
        index=True,
        doc="refresh token"
    )
    expires_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False,
        unique=False,
        index=True,
        doc="date expires"
    )
    user_agent = Column(
        String,
        nullable=True,
        unique=False,
        index=False,
        doc="user agent"
    )
    ip_address = Column(
        String,
        nullable=True,
        unique=False,
        index=False,
        doc="IP address"
    )
    dt_created = Column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False,
        unique=False,
        index=True,
        doc="Date and time of create (type TIMESTAMP)"
    )
    revoked = Column(
        BOOLEAN,
        nullable=False,
        unique=False,
        index=False,
        doc="revoked"
    )
