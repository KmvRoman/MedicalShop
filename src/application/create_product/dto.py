from dataclasses import dataclass


@dataclass
class CreateProductDtoInput:
    name: str
    quantity: int
    price: int
