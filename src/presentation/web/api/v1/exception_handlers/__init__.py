from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from src.application.common.exceptions import (
    EmployeeStatsIsEmpty, ClientStatsIsEmpty, ProductsNotFoundInOrder, ProductNotFound,
    ProductQuantityCannotBeLessWhenZero,
)
from src.presentation.web.api.v1.exception_handlers.db_error import db_error_handler
from src.presentation.web.api.v1.exception_handlers.error422 import http422_error_handler
from src.presentation.web.api.v1.exception_handlers.error400 import http_error_handler


def error_handlers_binder(app: FastAPI):
    app.add_exception_handler(RequestValidationError, http422_error_handler)
    app.add_exception_handler(EmployeeStatsIsEmpty, http_error_handler)
    app.add_exception_handler(ClientStatsIsEmpty, http_error_handler)
    app.add_exception_handler(ProductsNotFoundInOrder, http_error_handler)
    app.add_exception_handler(ProductNotFound, http_error_handler)
    app.add_exception_handler(ProductQuantityCannotBeLessWhenZero, http_error_handler)
    app.add_exception_handler(IntegrityError, db_error_handler)
