from dataclasses import dataclass
from typing import NewType, Optional

ProductId = NewType("ProductId", int)


@dataclass
class Product:
    id: Optional[ProductId]
    name: str
    quantity: int
    price: int
