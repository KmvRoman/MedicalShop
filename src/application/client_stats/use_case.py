from src.application.client_stats.dto import ReadClientStatisticDtoInput, ReadClientStatisticDtoOutput
from src.application.client_stats.interfaces import DbGateway
from src.application.common.exceptions import ClientStatsIsEmpty
from src.application.common.use_case import UseCase


class ReadClientStatisticCase(UseCase[ReadClientStatisticDtoInput, ReadClientStatisticDtoOutput]):
    def __init__(self, db_gateway: DbGateway):
        self.db_gateway = db_gateway

    async def __call__(self, data: ReadClientStatisticDtoInput) -> ReadClientStatisticDtoOutput:
        client_statistic = await self.db_gateway.read_client_statistics(
            client_id=data.client_id, year=data.year, month=data.month)
        if client_statistic is None:
            raise ClientStatsIsEmpty
        return ReadClientStatisticDtoOutput(
            client_id=client_statistic.client_id, name=client_statistic.name,
            quantity=client_statistic.quantity, amount=client_statistic.amount,
        )
