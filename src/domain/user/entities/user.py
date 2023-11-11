from dataclasses import dataclass
from datetime import date, datetime
from typing import NewType, Optional

UserId = NewType("UserId", int)


@dataclass
class User:
    id: Optional[UserId]
    full_name: str
    birthdate: date
    date_registration: datetime
