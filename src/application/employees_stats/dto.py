from dataclasses import dataclass

from src.domain.user.read.employee_stats import EmployeeStats


@dataclass
class ReadDtoStatisticsDtoInput:
    year: int
    month: int


@dataclass
class ReadDtoStatisticsDtoOutput:
    employees_statistics: list[EmployeeStats]
