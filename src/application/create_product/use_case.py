from src.application.common.use_case import UseCase
from src.application.create_product.dto import CreateProductDtoInput
from src.application.create_product.interfaces import DbGateway
from src.domain.product.entities.product import ProductId
from src.domain.product.services.product import ProductService


class CreateProductCase(UseCase[CreateProductDtoInput, ProductId]):
    def __init__(self, db_gateway: DbGateway, product_service: ProductService):
        self.db_gateway = db_gateway
        self.product_service = product_service

    async def __call__(self, data: CreateProductDtoInput) -> ProductId:
        product = self.product_service.create_product(
            name=data.name, quantity=data.quantity, price=data.price)
        product_id = await self.db_gateway.create_product(product)
        await self.db_gateway.commit()
        return ProductId(product_id)
