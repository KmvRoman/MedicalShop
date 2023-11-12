from datetime import datetime

from src.domain.order.entities.order import OrderProduct, Order
from src.domain.user.write.entities.client import ClientId


class OrderService:
    def create_order(self, client_id: ClientId, products: list[OrderProduct]) -> Order:
        price = 0
        new_product_list = []
        for product in products:
            if product.quantity >= 1:
                product.quantity -= 1
            else:
                continue
            price += product.price
            new_product_list.append(product)
        return Order(
            id=None, client_id=client_id, products=new_product_list,
            price=price, date=datetime.utcnow(),
        )
