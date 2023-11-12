from typing import Protocol

from src.application.client_stats.use_case import ReadClientStatisticCase
from src.application.create_client.use_case import CreateClientCase
from src.application.create_employee.use_case import CreateEmployeeCase
from src.application.create_order.use_case import CreateOrderCase
from src.application.create_product.use_case import CreateProductCase
from src.application.employee_stats.use_case import ReadEmployeeStatisticCase
from src.application.employees_stats.use_case import ReadEmployeesStatisticCase


class InteractorFactory(Protocol):

    async def client_stats(self) -> ReadClientStatisticCase:
        raise NotImplementedError

    async def employee_stats(self) -> ReadEmployeeStatisticCase:
        raise NotImplementedError

    async def employees_stats(self) -> ReadEmployeesStatisticCase:
        raise NotImplementedError

    async def create_client(self) -> CreateClientCase:
        raise NotImplementedError

    async def create_employee(self) -> CreateEmployeeCase:
        raise NotImplementedError

    async def create_product(self) -> CreateProductCase:
        raise NotImplementedError

    async def create_order(self) -> CreateOrderCase:
        raise NotImplementedError
