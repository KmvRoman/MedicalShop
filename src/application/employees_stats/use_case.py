from src.application.common.interfaces import ReadEmployeesStatistic
from src.application.common.use_case import UseCase
from src.application.employees_stats.dto import ReadDtoStatisticsDtoOutput, ReadDtoStatisticsDtoInput
from src.application.employees_stats.interfaces import DbGateway


class ReadEmployeesStatisticCase(UseCase[ReadDtoStatisticsDtoInput, ReadDtoStatisticsDtoOutput]):
    def __init__(self, db_gateway: DbGateway):
        self.db_gateway = db_gateway

    async def __call__(self, data: ReadDtoStatisticsDtoInput) -> ReadDtoStatisticsDtoOutput:
        employees_statistic = await self.db_gateway.read_employees_statistic(year=data.year, month=data.month)
        return ReadDtoStatisticsDtoOutput(employees_statistics=employees_statistic)
