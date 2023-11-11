from dataclasses import dataclass

from src.domain.user.read.employee_stats import EmployeeStats


@dataclass
class ReadEmployeesStatisticsDtoInput:
    year: int
    month: int


@dataclass
class ReadEmployeesStatisticsDtoOutput:
    employees_statistics: list[EmployeeStats]
