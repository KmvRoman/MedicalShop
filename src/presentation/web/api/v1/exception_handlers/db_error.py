from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


async def db_error_handler(_: Request, exc: IntegrityError) -> JSONResponse:
    return JSONResponse({"errors": [exc.args]}, status_code=400)