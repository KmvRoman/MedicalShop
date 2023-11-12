from datetime import date, datetime

from src.domain.user.write.entities.client import Client


class ClientService:
    def create_user(self, full_name: str, birthdate: date) -> Client:
        return Client(id=None, full_name=full_name, birthdate=birthdate, date_registration=datetime.utcnow())
