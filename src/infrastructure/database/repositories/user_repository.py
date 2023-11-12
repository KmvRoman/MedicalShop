from sqlalchemy import update

from src.application.common.exceptions import ProductNotFound
from src.domain.order.entities.order import Order, OrderId, OrderProduct, OrderProductIdent
from src.domain.product.entities.product import Product, ProductId
from src.domain.user.write.entities.client import Client, ClientId
from src.domain.user.write.entities.employee import Employee, EmployeeId
from src.infrastructure.database import ClientTable, EmployeeTable, ProductTable, OrderTable, OrderProductTable
from src.infrastructure.database.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def commit(self):
        await self.session.commit()

    async def create_client(self, client: Client) -> ClientId:
        client_instance = ClientTable(
            full_name=client.full_name, birthdate=client.birthdate,
            date_registration=client.date_registration,
        )
        self.session.add(client_instance)
        await self.session.flush()
        return client_instance.id

    async def create_employee(self, employee: Employee) -> EmployeeId:
        employee_instance = EmployeeTable(
            full_name=employee.full_name, birthdate=employee.birthdate,
            date_registration=employee.date_registration,
        )
        self.session.add(employee_instance)
        await self.session.flush()
        return employee_instance.id

    async def create_product(self, product: Product) -> ProductId:
        product_instance = ProductTable(name=product.name, quantity=product.quantity, price=product.price)
        self.session.add(product_instance)
        await self.session.flush()
        return product_instance.id

    async def create_order(self, order: Order) -> OrderId:
        order_instance = OrderTable(client_id=order.client_id, price=order.price, date=order.date)
        self.session.add(order_instance)
        await self.session.flush()
        for product in order.products:
            product_inst = await self.session.get(entity=ProductTable, ident=product.product_id)
            if product_inst.quantity >= 1:
                product_inst.quantity -= product.quantity
                order_instance.price += product.price
                product_order = OrderProductTable(
                    order_id=order_instance.id, employee_id=product.employee_id, product_id=product.product_id,
                )
                self.session.add(product_order)
        return order_instance.id

    async def add_price_to_product_order(
            self, products: list[OrderProductIdent]
    ) -> list[OrderProduct]:
        response_products = []
        for product in products:
            full_product = await self.session.get(ProductTable, ident=product.product_id)
            if full_product is None:
                return []
            new_product = OrderProduct(
                employee_id=product.employee_id, product_id=product.product_id,
                price=full_product.price, quantity=0,
            )
            response_products.append(new_product)
        return response_products

    async def update_quantity(self, product_id: ProductId, quantity: int) -> None:
        product = await self.session.get(entity=ProductTable, ident=product_id)
        if product is None:
            raise ProductNotFound
        product.quantity += quantity
