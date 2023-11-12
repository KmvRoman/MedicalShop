from datetime import datetime

from src.domain.order.entities.order import OrderProduct, Order
from src.domain.user.write.entities.client import ClientId


class OrderService:
    def create_order(self, client_id: ClientId, products: list[OrderProduct]) -> Order:
        new_product_list = []
        for product in products:
            product.quantity += 1
            new_product_list.append(product)
        return Order(
            id=None, client_id=client_id, products=new_product_list,
            price=0, date=datetime.utcnow(),
        )
