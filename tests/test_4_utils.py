from coe_6810110510.n4_utils import calculate_total
import unittest

class TestCalculateTotal(unittest.TestCase):
    def test_calculate_total_input_empty_cart_should_return_0(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_calculate_total_input_cart_with_items_should_return_correct_total(self):
        cart = [
            {"price": 10.0, "quantity": 2},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertEqual(calculate_total(cart), 35.0)

    def test_calculate_total_input_cart_with_discount_code_SAVE10_should_return_correct_total(self):
        cart = [
            {"price": 10.0, "quantity": 2},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertEqual(calculate_total(cart, discount_code="SAVE10"), 31.5)

    def test_calculate_total_input_cart_with_discount_code_SAVE20_should_return_correct_total(self):
        cart = [
            {"price": 10.0, "quantity": 2},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertEqual(calculate_total(cart, discount_code="SAVE20"), 35.0)

    def test_calculate_total_input_cart_with_missing_price_should_raise_value_error(self):
        cart = [
            {"quantity": 2},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertRaises(ValueError, calculate_total, cart)

    def test_calculate_total_input_cart_with_missing_quantity_should_raise_value_error(self):
        cart = [
            {"price": 10.0},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertRaises(ValueError, calculate_total, cart)

    def test_calculate_total_input_cart_with_non_numeric_price_should_raise_type_error(self):
        cart = [
            {"price": "10.0", "quantity": 2},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertRaises(TypeError, calculate_total, cart)

    def test_calculate_total_input_cart_with_non_integer_quantity_should_raise_type_error(self):
        cart = [
            {"price": 10.0, "quantity": 2.5},
            {"price": 5.0, "quantity": 3}
        ]
        self.assertRaises(TypeError, calculate_total, cart)

    def test_calculate_total_input_cart_non_list_should_raise_type_error(self):
        cart = "not a list"
        self.assertRaises(TypeError, calculate_total, cart)

    def test_calculate_total_input_cart_with_non_dict_item_should_raise_type_error(self):
        cart = [
            {"price": 10.0, "quantity": 2},
            "not a dict"
        ]
        self.assertRaises(TypeError, calculate_total, cart) 