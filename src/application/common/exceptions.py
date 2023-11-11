class ApplicationError(Exception):
    pass


class ClientStatsIsEmpty(ApplicationError):
    pass


class EmployeeStatsIsEmpty(ApplicationError):
    pass
