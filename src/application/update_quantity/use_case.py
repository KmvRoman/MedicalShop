from src.application.common.exceptions import ProductNotFound
from src.application.common.use_case import UseCase
from src.application.update_quantity.dto import UpdateQuantityDtoInput
from src.application.update_quantity.interfaces import DbGateway


class UpdateQuantityCase(UseCase[UpdateQuantityDtoInput, None]):
    def __init__(self, db_gateway: DbGateway):
        self.db_gateway = db_gateway

    async def __call__(self, data: UpdateQuantityDtoInput) -> None:
        await self.db_gateway.update_quantity(product_id=data.product_id, quantity=data.quantity_will_add)
        await self.db_gateway.commit()
