from starlette.requests import Request
from starlette.responses import JSONResponse

from src.application.common.exceptions import ApplicationError


async def http_error_handler(_: Request, exc: ApplicationError) -> JSONResponse:
    return JSONResponse({"errors": [exc.message]}, status_code=400)
