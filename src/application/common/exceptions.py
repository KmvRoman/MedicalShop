class ApplicationError(Exception):
    message: str


class ClientStatsIsEmpty(ApplicationError):
    message = "Client statistics not found"


class EmployeeStatsIsEmpty(ApplicationError):
    message = "Employee statistics not found"
