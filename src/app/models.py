import uuid
from dataclasses import dataclass, field
from typing import Optional


class InvalidProductError(ValueError):
    pass


@dataclass
class Product:
    name: str  #! must be at least 3 chars
    price: float  #! must be > 0
    quantity: int  #! must be > 0
    tags: Optional[list[str]] = field(default_factory=list)
    sku: uuid.UUID = field(default_factory=uuid.uuid4)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "tags": self.tags,
        }

    def __post_init__(self):
        if self.quantity < 1:
            raise InvalidProductError(
                f"[{self.sku}] Invalid product: quantity must be greater than 0"
            )
        if len(self.name) < 4:
            raise InvalidProductError(
                f"[{self.sku}] Invalid product: name must be at least 4 characters"
            )
        if self.price < 0:
            raise InvalidProductError(
                f"[{self.sku}] Invalid product: price must be greater than 0.00"
            )
