from dataclasses import dataclass

from src.domain.user.read.employee_stats import EmployeeStats


@dataclass
class ReadDtoStatisticsDtoOutput:
    employees_statistics: list[EmployeeStats]
