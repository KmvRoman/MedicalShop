from dataclasses import dataclass
from datetime import date, datetime
from typing import NewType, Optional

ClientId = NewType("UserId", int)


@dataclass
class Client:
    id: Optional[ClientId]
    full_name: str
    birthdate: date
    date_registration: datetime
