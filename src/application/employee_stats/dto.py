from dataclasses import dataclass

from src.domain.user.write.entities.employee import EmployeeId


@dataclass
class ReadEmployeeStatisticDtoInput:
    employee_id: EmployeeId


@dataclass
class ReadEmployeeStatisticDtoOutput:
    employee_id: EmployeeId
    name: str
    quantity: int
    unique_clients: int
    amount: int
