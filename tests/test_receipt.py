import pytest
from src.app.receipt import Receipt


class TestReceipt:

    def test_add_item(self):
        r = Receipt()
        r.add_item("Coffee", 4.50)
        assert r.subtotal() == 4.50
        assert "Coffee" in r.summary()

    def test_subtotal(self):
        r = Receipt()
        r.add_item("Coffee", 4.50)
        r.add_item("Muffin", 3.25)
        assert r.subtotal() == 7.75

    def test_total_with_tax(self):
        r = Receipt()
        r.add_item("Coffee", 4.50)
        r.add_item("Muffin", 3.25)
        total = r.total()
        expected = round((4.50 + 3.25) * 1.08, 2)
        assert total == pytest.approx(expected)

    def test_summary_output(self):
        r = Receipt()
        r.add_item("Coffee", 4.50)
        summary = r.summary()
        assert "Coffee" in summary
        assert "$4.50" in summary
        assert "Total" in summary
        assert "$4.86" in summary

    def test_empty_receipt(self):
        r = Receipt()
        assert r.subtotal() == 0.0
        assert r.tax() == 0.0
        assert r.total() == 0.0
