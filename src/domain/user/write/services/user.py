from datetime import date, datetime

from src.domain.user.write.entities.user import User


class UserService:
    def create_user(self, full_name: str, birthdate: date) -> User:
        return User(id=None, full_name=full_name, birthdate=birthdate, date_registration=datetime.utcnow())
