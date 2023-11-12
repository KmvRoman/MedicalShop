from src.application.common.exceptions import ProductsNotFoundInOrder
from src.application.common.use_case import UseCase
from src.application.create_order.dto import CreateOrderDtoInput
from src.application.create_order.interfaces import DbGateway
from src.domain.order.entities.order import OrderId
from src.domain.order.services.order import OrderService


class CreateOrderCase(UseCase[CreateOrderDtoInput, OrderId]):
    def __init__(self, db_gateway: DbGateway, order_service: OrderService):
        self.db_gateway = db_gateway
        self.order_service = order_service

    async def __call__(self, data: CreateOrderDtoInput) -> OrderId:
        products_with_price = await self.db_gateway.add_price_to_product_order(products=data.products)
        order = self.order_service.create_order(
            client_id=data.client_id, products=products_with_price,
        )
        if len(order.products) == 0:
            raise ProductsNotFoundInOrder
        order_id = await self.db_gateway.create_order(order=order)
        await self.db_gateway.commit()
        return OrderId(order_id)
