from dataclasses import dataclass

from src.domain.user.write.entities.user import UserId


@dataclass
class ReadClientStatisticDtoInput:
    client_id: UserId


@dataclass
class ReadClientStatisticDtoOutput:
    client_id: UserId
    name: str
    quantity: int
    amount: int
