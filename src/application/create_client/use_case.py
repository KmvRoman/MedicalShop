from src.application.common.use_case import UseCase
from src.application.create_client.dto import CreateClientDtoInput
from src.application.create_client.interfaces import DbGateway
from src.domain.user.write.entities.client import ClientId
from src.domain.user.write.services.client import ClientService


class CreateClientCase(UseCase[CreateClientDtoInput, ClientId]):
    def __init__(self, db_gateway: DbGateway, client_service: ClientService):
        self.db_gateway = db_gateway
        self.client_service = client_service

    async def __call__(self, data: CreateClientDtoInput) -> ClientId:
        client = self.client_service.create_user(full_name=data.full_name, birthdate=data.birthdate)
        client_id = await self.db_gateway.create_client(client=client)
        await self.db_gateway.commit()
        return ClientId(client_id)
