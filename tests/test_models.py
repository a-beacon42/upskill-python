import pytest
from src.app.models import Product, InvalidProductError


def test_valid_product():
    product_fields = {
        "name": "name",
        "price": 4.24,
        "quantity": 2,
        "tags": ["sale", "popular"],
    }
    new_prod = Product(**product_fields)
    assert new_prod.to_dict() == product_fields


def test_invalid_quantity_raises():
    bad_product_fields = {
        "name": "name",
        "price": 4.24,
        "quantity": 0,
        "tags": ["sale", "popular"],
    }
    with pytest.raises(InvalidProductError, match="quantity"):
        Product(**bad_product_fields)
