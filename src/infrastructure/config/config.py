from typing import Any

from attrs import define, field
from omegaconf import MISSING
from pydantic import PostgresDsn


def make_fastapi_instance_kwargs(settings: "ServerSettings") -> dict[str, Any]:
    if (
            settings.app_title == MISSING or
            settings.project_version == MISSING or
            settings.docs_url == MISSING or
            settings.redoc_url == MISSING):
        return {}

    return {
        "debug": True,
        "title": settings.app_title,
        "version": settings.project_version,
        "docs_url": settings.docs_url,
        "redoc_url": settings.redoc_url,
        "openapi_url": settings.openapi_root
        if not settings.is_in_prod
        else "/openapi.json",
    }


@define
class ServerSettings:
    app_title: str = MISSING
    project_version: str = MISSING
    docs_url: str = MISSING
    redoc_url: str = MISSING
    openapi_root: str = MISSING
    is_in_prod: bool = MISSING
    api_path_prefix: str = "/api/v1"

    host: str = MISSING
    port: int = MISSING


@define
class Database:
    user: str = MISSING
    password: str = MISSING
    db_name: str = MISSING
    host: str = MISSING

    connection_uri: str = field(default="")

    def __attrs_post_init__(self) -> None:
        sync_connection_url = PostgresDsn.build(
            scheme="postgresql",
            username=self.user,
            password=self.password,
            host=self.host,
            path=f"{self.db_name or ''}",
        )
        self.connection_uri = sync_connection_url.unicode_string().replace("postgresql", "postgresql+asyncpg")


@define
class Config:
    server: ServerSettings = ServerSettings()
    database: Database = Database()
