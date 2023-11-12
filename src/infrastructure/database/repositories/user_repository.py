from src.domain.order.entities.order import Order, OrderId, OrderProduct, OrderProductWithPrice
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
            product_instance = OrderProductTable(
                order_id=order_instance.id, employee_id=product.employee, product_id=product.product,
            )
            self.session.add(product_instance)
        return order_instance.id

    async def add_price_to_product_order(
            self, products: list[OrderProduct]
    ) -> list[OrderProductWithPrice]:
        response_products = []
        for product in products:
            full_product = await self.session.get(ProductTable, ident=product.product)
            if full_product is None:
                return []
            new_product = OrderProductWithPrice(
                employee_id=product.employee, product_id=product.product,
                price=full_product.price,
            )
            response_products.append(new_product)
        return response_products
