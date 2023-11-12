from datetime import date, datetime

from pydantic import BaseModel, Field

from src.domain.product.entities.product import ProductId
from src.domain.user.write.entities.client import ClientId
from src.domain.user.write.entities.employee import EmployeeId


class CreateClientRequest(BaseModel):
    full_name: str = Field(max_length=100)
    birthdate: date


class CreateEmployeeRequest(BaseModel):
    full_name: str = Field(max_length=100)
    birthdate: date


class CreateProductRequest(BaseModel):
    name: str = Field(max_length=255)
    quantity: int
    price: int


class ProductOrderRequest(BaseModel):
    employee: EmployeeId
    product: ProductId


class CreateOrderRequest(BaseModel):
    client_id: ClientId
    date: datetime
    products: list[ProductOrderRequest]


class UpdateProductQuantity(BaseModel):
    product_id: ProductId
    quantity_add: int
