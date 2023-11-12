from typing import Protocol

from src.domain.user.read.client_stats import ClientStats
from src.domain.user.read.employee_stats import EmployeeStats
from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.entities.client import ClientId


class ReadClientStatistic(Protocol):
    async def read_client_statistics(self, client_id: ClientId, year: int, month: int) -> ClientStats | None:
        raise NotImplementedError


class ReadEmployeeStatistic(Protocol):
    async def read_employee_statistic(self, employee_id: EmployeeId, year: int, month: int) -> EmployeeStats | None:
        raise NotImplementedError


class ReadEmployeesStatistic(Protocol):
    async def read_employees_statistic(self, year: int, month: int) -> list[EmployeeStats]:
        raise NotImplementedError
