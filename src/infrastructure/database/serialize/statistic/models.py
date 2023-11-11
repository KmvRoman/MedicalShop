from typing import NamedTuple

from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.entities.user import UserId


class EmployeeStatistic(NamedTuple):
    employee_id: EmployeeId
    name: str
    unique_clients: int
    product_count: int
    amount: int


class ClientStatistic(NamedTuple):
    client_id: UserId
    name: str
    product_count: int
    amount: int
