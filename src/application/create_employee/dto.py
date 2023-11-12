from dataclasses import dataclass
from datetime import date


@dataclass
class CreateEmployeeDtoInput:
    full_name: str
    birthdate: date
