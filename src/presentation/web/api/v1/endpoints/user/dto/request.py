from datetime import date, datetime

from pydantic import BaseModel

from src.domain.product.entities.product import ProductId
from src.domain.user.write.entities.client import ClientId
from src.domain.user.write.entities.employee import EmployeeId


class CreateClientRequest(BaseModel):
    full_name: str
    birthdate: date


class CreateEmployeeRequest(BaseModel):
    full_name: str
    birthdate: date


class CreateProductRequest(BaseModel):
    name: str
    quantity: int
    price: int


class ProductOrderRequest(BaseModel):
    employee: EmployeeId
    product: ProductId


class CreateOrderRequest(BaseModel):
    client_id: ClientId
    date: datetime
    products: list[ProductOrderRequest]
