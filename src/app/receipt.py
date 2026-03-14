from dataclasses import dataclass, field


@dataclass
class LineItem:
    name: str
    price: float


@dataclass
class Receipt:
    items: list[LineItem] = field(default_factory=list)
    tax_rate: float = 0.08

    def add_item(self, name: str, price: float) -> None:
        self.items.append(LineItem(name=name, price=price))

    def subtotal(self) -> float:
        return round(sum(item.price for item in self.items), 2)

    def tax(self) -> float:
        return round(self.subtotal() * self.tax_rate, 2)

    def total(self) -> float:
        return round(self.subtotal() + self.tax(), 2)

    def summary(self) -> str:
        lines = [f"  {item.name}: ${item.price:.2f}" for item in self.items]
        lines.append(f"  Subtotal: ${self.subtotal():.2f}")
        lines.append(f"  Tax: ${self.tax():.2f}")
        lines.append(f"  Total: ${self.total():.2f}")
        return "\n".join(lines)
