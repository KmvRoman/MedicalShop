from dataclasses import dataclass

from src.domain.user.write.entities.employee import EmployeeId


@dataclass
class EmployeeStats:
    employee_id: EmployeeId
    name: str
    unique_clients: int
    quantity: int
    amount: int
