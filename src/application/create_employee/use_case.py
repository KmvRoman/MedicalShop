from src.application.common.use_case import UseCase
from src.application.create_employee.dto import CreateEmployeeDtoInput
from src.application.create_employee.interfaces import DbGateway
from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.services.employee import EmployeeService


class CreateEmployeeCase(UseCase[CreateEmployeeDtoInput, EmployeeId]):
    def __init__(self, db_gateway: DbGateway, employee_service: EmployeeService):
        self.db_gateway = db_gateway
        self.employee_service = employee_service

    async def __call__(self, data: CreateEmployeeDtoInput) -> EmployeeId:
        employee = self.employee_service.create_employee(full_name=data.full_name, birthdate=data.birthdate)
        employee_id = await self.db_gateway.create_employee(employee=employee)
        await self.db_gateway.commit()
        return EmployeeId(employee_id)
