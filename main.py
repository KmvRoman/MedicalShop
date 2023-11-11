from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import uvicorn

from src.infrastructure.config.config import make_fastapi_instance_kwargs
from src.infrastructure.config.parse_config import load_config, BASE_DIR
from src.infrastructure.database.repositories.statistic import StatisticRepository
from src.infrastructure.ioc.ioc import IOC
from src.presentation.web.api.v1 import routers
from src.presentation.web.api.v1.dependencies.dependencies import IocDependencyMarker
from src.presentation.web.api.v1.exception_handlers import error_handlers_binder
from src.presentation.web.api.v1.exception_handlers.error422 import http422_error_handler
from src.presentation.web.api.v1.exception_handlers.error400 import http_error_handler


def main():
    config = load_config(BASE_DIR / "infrastructure" / "config" / "config.yaml")
    app = FastAPI(
        **make_fastapi_instance_kwargs(config.server)
    )
    error_handlers_binder(app=app)
    engine = create_async_engine(url=config.database.connection_uri)
    session_make = sessionmaker(  # NOQA
        engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
    )
    stat_repo = StatisticRepository(session_or_pool=session_make)
    ioc = IOC(statistic_repo=stat_repo)
    [app.include_router(router) for router in routers]
    app.dependency_overrides.update(
        {
            IocDependencyMarker: lambda: ioc,
        }
    )
    uvicorn.run(app=app, host=config.server.host, port=config.server.port)


if __name__ == '__main__':
    main()
