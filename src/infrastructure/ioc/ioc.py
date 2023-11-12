from src.application.create_client.use_case import CreateClientCase
from src.application.create_employee.use_case import CreateEmployeeCase
from src.application.create_order.use_case import CreateOrderCase
from src.application.create_product.use_case import CreateProductCase
from src.domain.order.services.order import OrderService
from src.domain.product.services.product import ProductService
from src.domain.user.write.services.client import ClientService
from src.domain.user.write.services.employee import EmployeeService
from src.infrastructure.database.repositories.statistic import StatisticRepository
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.infrastructure.ioc.interfaces import InteractorFactory

from src.application.client_stats.use_case import ReadClientStatisticCase
from src.application.employee_stats.use_case import ReadEmployeeStatisticCase
from src.application.employees_stats.use_case import ReadEmployeesStatisticCase


class IOC(InteractorFactory):
    def __init__(self, statistic_repo: StatisticRepository, user_repo: UserRepository):
        self.stat_repo = statistic_repo
        self.user_repo = user_repo
        self.client_service = ClientService()
        self.employee_service = EmployeeService()
        self.product_service = ProductService()
        self.order_service = OrderService()

    async def client_stats(self) -> ReadClientStatisticCase:
        return ReadClientStatisticCase(db_gateway=self.stat_repo)

    async def employee_stats(self) -> ReadEmployeeStatisticCase:
        return ReadEmployeeStatisticCase(db_gateway=self.stat_repo)

    async def employees_stats(self) -> ReadEmployeesStatisticCase:
        return ReadEmployeesStatisticCase(db_gateway=self.stat_repo)

    async def create_client(self) -> CreateClientCase:
        return CreateClientCase(db_gateway=self.user_repo, client_service=self.client_service)

    async def create_employee(self) -> CreateEmployeeCase:
        return CreateEmployeeCase(db_gateway=self.user_repo, employee_service=self.employee_service)

    async def create_product(self) -> CreateProductCase:
        return CreateProductCase(db_gateway=self.user_repo, product_service=self.product_service)

    async def create_order(self) -> CreateOrderCase:
        return CreateOrderCase(db_gateway=self.user_repo, order_service=self.order_service)
