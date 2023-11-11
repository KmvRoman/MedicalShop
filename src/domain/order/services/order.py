from datetime import datetime

from src.domain.order.entities.order import OrderProduct, Order


class OrderService:
    def create_order(self, products: list[OrderProduct], price: int) -> Order:
        return Order(id=None, products=products, price=price, date=datetime.utcnow())
