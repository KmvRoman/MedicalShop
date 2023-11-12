from dataclasses import dataclass
from datetime import datetime

from src.domain.order.entities.order import OrderProductIdent
from src.domain.user.write.entities.client import ClientId


@dataclass
class CreateOrderDtoInput:
    client_id: ClientId
    date: datetime
    products: list[OrderProductIdent]
