from fastapi import APIRouter, Depends

from src.application.client_stats.dto import ReadClientStatisticDtoInput
from src.application.employee_stats.dto import ReadEmployeeStatisticDtoInput
from src.application.employees_stats.dto import ReadEmployeesStatisticsDtoInput
from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.entities.user import UserId
from src.infrastructure.ioc.interfaces import InteractorFactory
from src.presentation.web.api.v1.dependencies.dependencies import IocDependencyMarker
from src.presentation.web.api.v1.endpoints.statistic.dto.response import EmployeeStatsResponse, EmployeesStatsResponse, \
    ClientStatsResponse

router = APIRouter(prefix="/api/v1", tags=["Statistic"])


@router.get(path="/statistics/employee/{id}")
async def get_employee_stats(
        id: int, month: int, year: int, ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> EmployeeStatsResponse:
    statistics = await ioc.employee_stats()
    employee_stats = await statistics(
        data=ReadEmployeeStatisticDtoInput(
            employee_id=EmployeeId(id),
            year=year, month=month,
        )
    )
    return EmployeeStatsResponse(
        full_name=employee_stats.name, quantity=employee_stats.quantity,
        unique_clients=employee_stats.unique_clients, amount=employee_stats.amount,
    )


@router.get(path="/employee/statistics/")
async def get_employees_stats(
        month: int, year: int, ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> list[EmployeesStatsResponse]:
    statistics = await ioc.employees_stats()
    employees_stats = await statistics(data=ReadEmployeesStatisticsDtoInput(year=year, month=month))
    return [EmployeesStatsResponse(
        id=stat.employee_id, full_name=stat.name,
        quantity=stat.quantity, unique_clients=stat.unique_clients, amount=stat.amount,
    ) for stat in employees_stats.employees_statistics]


@router.get(path="/statistics/client/{id}")
async def get_client_stats(
        id: int, month: int, year: int,
        ioc: InteractorFactory = Depends(IocDependencyMarker),
) -> ClientStatsResponse:
    statistics = await ioc.client_stats()
    client_stats = await statistics(
        data=ReadClientStatisticDtoInput(
            client_id=UserId(id), year=year, month=month,
        )
    )
    return ClientStatsResponse(
        id=client_stats.client_id, full_name=client_stats.name,
        quantity=client_stats.quantity, amount=client_stats.amount,
    )
