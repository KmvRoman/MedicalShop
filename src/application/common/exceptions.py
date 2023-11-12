class ApplicationError(Exception):
    message: str


class ClientStatsIsEmpty(ApplicationError):
    message = "Client statistics not found"


class EmployeeStatsIsEmpty(ApplicationError):
    message = "Employee statistics not found"


class ProductsNotFoundInOrder(ApplicationError):
    message = "You must input at least one product"


class ProductNotFound(ApplicationError):
    message = "Product not found"
