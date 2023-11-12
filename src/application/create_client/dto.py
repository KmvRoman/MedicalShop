from dataclasses import dataclass
from datetime import date


@dataclass
class CreateClientDtoInput:
    full_name: str
    birthdate: date
