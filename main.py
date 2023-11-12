from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import uvicorn

from src.infrastructure.config.config import make_fastapi_instance_kwargs
from src.infrastructure.config.parse_config import load_config, BASE_DIR
from src.infrastructure.database.repositories.statistic import StatisticRepository
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.infrastructure.ioc.ioc import IOC
from src.presentation.web.api.v1 import routers
from src.presentation.web.api.v1.dependencies.dependencies import IocDependencyMarker
from src.presentation.web.api.v1.exception_handlers import error_handlers_binder
from src.presentation.web.gunicorn_starter import StandaloneApplication


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
    user_repo = UserRepository(session_or_pool=session_make)
    ioc = IOC(statistic_repo=stat_repo, user_repo=user_repo)
    [app.include_router(router) for router in routers]
    app.dependency_overrides.update(
        {
            IocDependencyMarker: lambda: ioc,
        }
    )
    options = {
        "bind": "%s:%s" % (config.server.host, config.server.port),
        "worker_class": "uvicorn.workers.UvicornWorker",
        "reload": True,
        "disable_existing_loggers": False,
        "preload_app": True,
    }
    gunicorn_app = StandaloneApplication(app, options)
    gunicorn_app.run()
    # uvicorn.run(app=app, host=config.server.host, port=config.server.port)


if __name__ == '__main__':
    main()
