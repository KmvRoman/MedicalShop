from pydantic import BaseModel

from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.entities.client import ClientId


class EmployeeStatsResponse(BaseModel):
    full_name: str
    quantity: int
    unique_clients: int
    amount: int


class EmployeesStatsResponse(BaseModel):
    id: EmployeeId
    full_name: str
    quantity: int
    unique_clients: int
    amount: int


class ClientStatsResponse(BaseModel):
    id: ClientId
    full_name: str
    quantity: int
    amount: int
