from datetime import date, datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import BIGINT, Identity, VARCHAR, DATE, TIMESTAMP

from src.infrastructure.database.models.base import Base


class ClientTable(Base):
    id: Mapped[int] = mapped_column(BIGINT, Identity(always=True, cache=1), primary_key=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    birthdate: Mapped[date] = mapped_column(DATE, nullable=False)
    date_registration: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
