from datetime import date
from typing import Protocol

from src.domain.order.entities.order import Order, OrderId, OrderProduct, OrderProductWithPrice
from src.domain.product.entities.product import Product, ProductId
from src.domain.user.read.client_stats import ClientStats
from src.domain.user.read.employee_stats import EmployeeStats
from src.domain.user.write.entities.employee import EmployeeId, Employee
from src.domain.user.write.entities.client import ClientId, Client


class ReadClientStatistic(Protocol):
    async def read_client_statistics(self, client_id: ClientId, year: int, month: int) -> ClientStats | None:
        raise NotImplementedError


class ReadEmployeeStatistic(Protocol):
    async def read_employee_statistic(self, employee_id: EmployeeId, year: int, month: int) -> EmployeeStats | None:
        raise NotImplementedError


class ReadEmployeesStatistic(Protocol):
    async def read_employees_statistic(self, year: int, month: int) -> list[EmployeeStats]:
        raise NotImplementedError


class Committer(Protocol):
    async def commit(self):
        raise NotImplementedError


class CreateClient(Protocol):
    async def create_client(self, client: Client) -> ClientId:
        raise NotImplementedError


class CreateEmployee(Protocol):
    async def create_employee(self, employee: Employee) -> EmployeeId:
        raise NotImplementedError


class CreateProduct(Protocol):
    async def create_product(self, product: Product) -> ProductId:
        raise NotImplementedError


class CreateOrder(Protocol):
    async def create_order(self, order: Order) -> OrderId:
        raise NotImplementedError


class AddPriceToOrderProduct(Product):
    async def add_price_to_product_order(
            self, products: list[OrderProduct]
    ) -> list[OrderProductWithPrice]:
        raise NotImplementedError
