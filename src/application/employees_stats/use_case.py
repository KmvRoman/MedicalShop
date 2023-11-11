from src.application.common.interfaces import ReadEmployeesStatistic
from src.application.common.use_case import UseCase
from src.application.employees_stats.dto import ReadDtoStatisticsDtoOutput
from src.application.employees_stats.interfaces import DbGateway


class ReadEmployeesStatisticCase(UseCase[ReadDtoStatisticsDtoOutput]):
    def __init__(self, db_gateway: DbGateway):
        self.db_gateway = db_gateway

    async def __call__(self) -> ReadDtoStatisticsDtoOutput:
        employees_statistic = await self.db_gateway.read_employees_statistic()
        return ReadDtoStatisticsDtoOutput(employees_statistics=employees_statistic)
