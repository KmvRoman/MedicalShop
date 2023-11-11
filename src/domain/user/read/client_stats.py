from dataclasses import dataclass

from src.domain.user.write.entities.user import UserId


@dataclass
class ClientStats:
    client_id: UserId
    name: str
    quantity: int
    amount: int
