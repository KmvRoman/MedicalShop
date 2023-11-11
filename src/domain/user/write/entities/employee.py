from dataclasses import dataclass
from datetime import date, datetime
from typing import NewType, Optional

EmployeeId = NewType("EmployeeId", int)


@dataclass
class Employee:
    id: Optional[EmployeeId]
    full_name: str
    birthdate: date
    date_registration: datetime
