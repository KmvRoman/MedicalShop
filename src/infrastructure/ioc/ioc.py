from src.infrastructure.database.repositories.statistic import StatisticRepository
from src.infrastructure.ioc.interfaces import InteractorFactory

from src.application.client_stats.use_case import ReadClientStatisticCase
from src.application.employee_stats.use_case import ReadEmployeeStatisticCase
from src.application.employees_stats.use_case import ReadEmployeesStatisticCase


class IOC(InteractorFactory):
    def __init__(self, statistic_repo: StatisticRepository):
        self.stat_repo = statistic_repo

    async def client_stats(self) -> ReadClientStatisticCase:
        return ReadClientStatisticCase(db_gateway=self.stat_repo)

    async def employee_stats(self) -> ReadEmployeeStatisticCase:
        return ReadEmployeeStatisticCase(db_gateway=self.stat_repo)

    async def employees_stats(self) -> ReadEmployeesStatisticCase:
        return ReadEmployeesStatisticCase(db_gateway=self.stat_repo)
