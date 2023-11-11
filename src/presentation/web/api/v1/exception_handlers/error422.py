from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http422_error_handler(
        _: Request,
        exc: RequestValidationError | ValidationError,
) -> JSONResponse:
    try:
        return JSONResponse(
            {"errors": exc.errors()},
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        )
    except TypeError:
        return JSONResponse(
            {"errors": exc.json()},
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        )
