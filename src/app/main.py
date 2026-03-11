from models import Product, InvalidProductError
from services import Inventory


def main():
    # Tests — run after your solution
    inv = Inventory()

    # Valid products
    prods = [
        {"name": "Gidget", "price": 1.11, "quantity": 2, "tags": ["sale", "popular"]},
        {"name": "Gadget", "price": 24.50, "quantity": 3, "tags": ["new"]},
        {"name": "Doohickey", "price": 4.75, "quantity": 10, "tags": ["sale"]},
    ]
    for prod in prods:
        new_prod = Product(**prod)
        inv.add(new_prod)

    # Lookups
    all_products = inv.get_all()
    first_prod = all_products[0]
    print(inv.get(first_prod.sku))
    # Expected: Product(name='Gidget', price=1.11, quantity=2, tags=['sale', 'popular'])

    print(inv.search_by_tag("sale"))
    # Expected: [Gidget, Doohickey]

    print(inv.total_value())
    # Expected: 171.45  (9.99*5 + 24.50*3 + 4.75*10)

    # Invalid cases — each should raise InvalidProductError
    bad_inputs = [
        {"name": "Negative Price", "price": -5.0, "quantity": 1},
        {"name": "Negative Qty", "price": 1.0, "quantity": -1},
        {"name": "Duplicate", "price": 1.0, "quantity": 1, "sku": inv.get_all()[0].sku},
    ]
    for bad in bad_inputs:
        try:
            bad_prod = Product(**bad)
            inv.add(bad_prod)
            print(f"BUG: {bad_prod.sku or '(empty)'} should have been rejected")
        except InvalidProductError as e:
            print(f"Caught: {e}")


if __name__ == "__main__":
    main()
