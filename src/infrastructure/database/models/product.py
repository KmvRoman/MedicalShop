from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import BIGINT, Identity, VARCHAR, INTEGER

from src.infrastructure.database.models.base import Base


class ProductTable(Base):
    id: Mapped[int] = mapped_column(BIGINT, Identity(always=True, cache=1), primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    quantity: Mapped[int] = mapped_column(INTEGER, nullable=False)
    price: Mapped[int] = mapped_column(INTEGER, nullable=False)
