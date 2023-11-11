from datetime import date, datetime

from src.domain.user.entities.employee import Employee


class EmployeeService:
    def create_employee(self, full_name: str, birthdate: date) -> Employee:
        return Employee(id=None, full_name=full_name, birthdate=birthdate, date_registration=datetime.utcnow())
