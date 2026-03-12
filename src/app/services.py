from src.app.models import Product, InvalidProductError
import uuid


class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        if self.get(sku=product.sku):
            raise InvalidProductError(f"[{product.sku}] Duplicate SKU")
        try:
            self.products.append(product)
        except Exception as e:
            raise InvalidProductError(e)

    def get(self, sku: uuid.UUID) -> Product | None:
        for prod in self.products:
            if prod.sku == sku:
                return prod
        return None

    def get_all(self) -> list[Product]:
        return self.products

    def search_by_tag(self, selectedTag: str) -> list[Product]:
        matching_tags = []
        for product in self.products:
            if product.tags:
                for tag in product.tags:
                    if tag == selectedTag:
                        matching_tags.append(product)
        return matching_tags

    def total_value(self) -> float:
        total = 0.00
        for prod in self.products:
            cost = prod.quantity * prod.price
            total += cost
        return round(total, 2)

    def remove(self, sku: uuid.UUID) -> Product | None:
        try:
            prod_to_delete = self.get(sku)
            if prod_to_delete:
                self.products = [
                    prod for prod in self.products if prod.sku != prod_to_delete.sku
                ]
        except Exception as e:
            raise KeyError(e)
