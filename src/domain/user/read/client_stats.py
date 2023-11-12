from dataclasses import dataclass

from src.domain.user.write.entities.client import ClientId


@dataclass
class ClientStats:
    client_id: ClientId
    name: str
    quantity: int
    amount: int
