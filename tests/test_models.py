import pytest
from src.app.models import Product, InvalidProductError

good_prod = {
    "name": "name",
    "price": 4.24,
    "quantity": 2,
    "tags": ["sale", "popular"],
}
no_tags = {
    "name": "name",
    "price": 4.24,
    "quantity": 2,
}


@pytest.mark.parametrize(
    "input_prod", [good_prod, no_tags], ids=["good_prod", "no_tags"]
)
def test_valid_product(input_prod):
    new_prod = Product(**input_prod)
    assert new_prod.name == input_prod["name"]
    assert new_prod.price == input_prod["price"]
    assert new_prod.quantity == input_prod["quantity"]
    if input_prod.get("tags"):
        assert new_prod.tags == input_prod.get("tags")
    else:
        assert new_prod.tags == []


low_quantity = {
    "name": "name",
    "price": 4.24,
    "quantity": 0,
    "tags": ["sale", "popular"],
}
short_name = {
    "name": "xx",
    "price": 4.24,
    "quantity": 10,
    "tags": ["sale", "popular"],
}
low_price = {
    "name": "name",
    "price": -10,
    "quantity": 10,
    "tags": ["sale", "popular"],
}


@pytest.mark.parametrize(
    "bad_product, match_str",
    [(low_quantity, "quantity"), (short_name, "name"), (low_price, "price")],
    ids=["low_quantity", "short_name", "low_price"],
)
def test_invalid_quantity_raises(bad_product, match_str):
    with pytest.raises(InvalidProductError, match=match_str):
        Product(**bad_product)
