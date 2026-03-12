import pytest
from src.app.models import Product
from src.app.services import Inventory, InvalidProductError


@pytest.fixture()
def inventory() -> Inventory:
    inv = Inventory()

    prods = [
        {"name": "Gidget", "price": 1.11, "quantity": 2, "tags": ["sale", "popular"]},
        {"name": "Gadget", "price": 24.50, "quantity": 3, "tags": ["new"]},
        {"name": "Doohickey", "price": 4.75, "quantity": 10, "tags": ["sale"]},
    ]
    for prod in prods:
        new_prod = Product(**prod)
        inv.add(new_prod)

    return inv


def test_add_product(inventory):
    new_prod = {"name": "flicky", "price": 75, "quantity": 8, "tags": ["popular"]}
    inventory.add(Product(**new_prod))

    all_prods = inventory.get_all()
    assert new_prod["name"] in [prod.name for prod in all_prods]


# valid + return None
def test_get_product_by_sku(inventory):
    existing = inventory.get_all()[0]
    found = inventory.get(existing.sku)
    assert found is not None
    assert found.name == existing.name

    import uuid

    assert inventory.get(uuid.uuid4()) is None


def test_duplicate_sku(inventory):
    existing = inventory.get_all()[0]
    with pytest.raises(InvalidProductError):
        inventory.add(existing)


def test_search_by_tag(inventory):
    results = inventory.search_by_tag("sale")
    assert len(results) == 2
    assert results[0].name == "Gidget"
    assert results[1].name == "Doohickey"
    assert "sale" in results[0].tags
    assert "sale" in results[1].tags


def test_total_value(inventory):
    total = inventory.total_value()
    # 1.11*2 + 24.50*3 + 4.75*10 = 123.22
    assert total == pytest.approx(123.22)
