from dataclasses import dataclass
from datetime import datetime
from typing import NewType, Optional

from src.domain.product.entities.product import ProductId
from src.domain.user.entities.employee import EmployeeId

OrderId = NewType("OrderId", int)


@dataclass
class OrderProduct:
    employee: EmployeeId
    product: ProductId


@dataclass
class Order:
    id: Optional[OrderId]
    products: list[OrderProduct]
    price: int
    date: datetime
