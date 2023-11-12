from datetime import datetime

from src.domain.order.entities.order import OrderProduct, Order, OrderProductWithPrice
from src.domain.user.write.entities.client import ClientId


class OrderService:
    def create_order(self, client_id: ClientId, products: list[OrderProductWithPrice]) -> Order:
        price = 0
        for product in products:
            price += product.price
        return Order(
            id=None, client_id=client_id, products=[
                OrderProduct(employee=pr.employee_id, product=pr.product_id) for pr in products
            ],
            price=price, date=datetime.utcnow(),
        )
