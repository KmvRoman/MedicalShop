from dataclasses import dataclass

from src.domain.product.entities.product import ProductId


@dataclass
class UpdateQuantityDtoInput:
    product_id: ProductId
    quantity_will_add: int
