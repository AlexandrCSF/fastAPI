from datetime import datetime
from uuid import UUID

import uuid

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from db.base_class import Base


class UserModel(Base):
    __tablename__="usermodel"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    uuid: Mapped[UUID] = mapped_column(default=uuid.uuid4, unique=True,nullable=False)
    first_name: Mapped[str] = mapped_column(String(255),default=None,nullable=True)
    last_name: Mapped[str] = mapped_column(String(255),default=None,nullable=True)
    username: Mapped[str] = mapped_column(String(255),default=None,nullable=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
