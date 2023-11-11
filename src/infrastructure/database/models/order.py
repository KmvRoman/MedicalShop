from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import BIGINT, Identity, TIMESTAMP, ForeignKey

from src.infrastructure.database.models.base import Base


class OrderTable(Base):
    id: Mapped[int] = mapped_column(BIGINT, Identity(always=True, cache=1), primary_key=True)
    client_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey(column="clienttable.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    price: Mapped[int] = mapped_column(BIGINT, nullable=False)
    date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
