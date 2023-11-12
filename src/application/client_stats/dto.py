from dataclasses import dataclass

from src.domain.user.write.entities.client import ClientId


@dataclass
class ReadClientStatisticDtoInput:
    client_id: ClientId
    year: int
    month: int


@dataclass
class ReadClientStatisticDtoOutput:
    client_id: ClientId
    name: str
    quantity: int
    amount: int
