from typing import Protocol

from src.application.client_stats.use_case import ReadClientStatisticCase
from src.application.employee_stats.use_case import ReadEmployeeStatisticCase
from src.application.employees_stats.use_case import ReadEmployeesStatisticCase


class InteractorFactory(Protocol):

    async def client_stats(self) -> ReadClientStatisticCase:
        raise NotImplementedError

    async def employee_stats(self) -> ReadEmployeeStatisticCase:
        raise NotImplementedError

    async def employees_stats(self) -> ReadEmployeesStatisticCase:
        raise NotImplementedError
