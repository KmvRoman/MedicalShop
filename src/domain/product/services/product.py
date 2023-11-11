from src.domain.product.entities.product import Product


class ProductService:
    def create_product(self, name: str, quantity: int, price: int) -> Product:
        return Product(id=None, name=name, quantity=quantity, price=price)
