from src.application.common.exceptions import EmployeeStatsIsEmpty
from src.application.common.use_case import UseCase
from src.application.employee_stats.dto import ReadEmployeeStatisticDtoOutput, ReadEmployeeStatisticDtoInput
from src.application.employee_stats.interfaces import DbGateway


class ReadEmployeeStatisticCase(UseCase[ReadEmployeeStatisticDtoInput, ReadEmployeeStatisticDtoOutput]):
    def __init__(self, db_gateway: DbGateway):
        self.db_gateway = db_gateway

    async def __call__(self, data: ReadEmployeeStatisticDtoInput) -> ReadEmployeeStatisticDtoOutput:
        employee_statistic = await self.db_gateway.read_employee_statistic(
            employee_id=data.employee_id, year=data.year, month=data.month)
        if employee_statistic is None:
            raise EmployeeStatsIsEmpty
        return ReadEmployeeStatisticDtoOutput(
            employee_id=employee_statistic.employee_id, name=employee_statistic.name,
            quantity=employee_statistic.quantity, unique_clients=employee_statistic.unique_clients,
            amount=employee_statistic.amount,
        )
