from src.domain.user.read.client_stats import ClientStats
from src.domain.user.read.employee_stats import EmployeeStats
from src.infrastructure.database.serialize.statistic.models import EmployeeStatistic, ClientStatistic


def serialize_employees_statistic(payload: list[tuple]) -> list[EmployeeStats]:
    response = []
    for s in payload:
        employee_stats = EmployeeStatistic(*s)
        response.append(EmployeeStats(
            employee_id=employee_stats.employee_id, name=employee_stats.name,
            unique_clients=employee_stats.unique_clients, quantity=employee_stats.product_count,
            amount=employee_stats.amount,
        ))
    return response


def serialize_employee_statistic(payload: list[tuple]) -> EmployeeStats | None:
    if len(payload) == 0:
        return None
    employee_stats = EmployeeStatistic(*payload[0])
    return EmployeeStats(
        employee_id=employee_stats.employee_id, name=employee_stats.name,
        unique_clients=employee_stats.unique_clients, quantity=employee_stats.product_count,
        amount=employee_stats.amount,
    )


def serialize_client_statistic(payload: list[tuple]) -> ClientStats | None:
    if len(payload) == 0:
        return None
    client_stats = ClientStatistic(*payload[0])
    return ClientStats(
        client_id=client_stats.client_id, name=client_stats.name,
        quantity=client_stats.product_count,
        amount=client_stats.amount,
    )
