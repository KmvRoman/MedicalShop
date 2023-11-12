from dataclasses import dataclass
from datetime import datetime
from typing import NewType, Optional

from src.domain.product.entities.product import ProductId
from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.entities.client import ClientId

OrderId = NewType("OrderId", int)


@dataclass
class OrderProductIdent:
    employee_id: EmployeeId
    product_id: ProductId


@dataclass
class OrderProduct:
    employee_id: EmployeeId
    product_id: ProductId
    quantity: int
    price: int


@dataclass
class Order:
    id: Optional[OrderId]
    client_id: ClientId
    products: list[OrderProduct]
    price: int
    date: datetime
