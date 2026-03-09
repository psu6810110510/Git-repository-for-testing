from coe_6810110510.n5_utils import calculate_taxi_fare
import unittest

class TestCalculateTaxiFare(unittest.TestCase):
    def test_calculate_taxi_fare_input_distance_5_should_return_(self):
        self.assertEqual(calculate_taxi_fare(5, 0), 59.0)

    def test_calculate_taxi_fare_input_distance_10_should_return_89(self):
        self.assertEqual(calculate_taxi_fare(10, 0), 89.0)

    def test_calculate_taxi_fare_input_distance_0_should_return_35(self):
        self.assertEqual(calculate_taxi_fare(0, 0), 35.0)

    def test_calculate_taxi_fare_input_distance_negative_should_raise_value_error(self):
        self.assertRaises(ValueError, calculate_taxi_fare, -5, 0)

    def test_calculate_taxi_fare_input_distance_non_numeric_should_raise_type_error(self):
        self.assertRaises(TypeError, calculate_taxi_fare, "five", 0)

    def test_calculate_taxi_fare_input_distance_with_decimal_should_return_correct_fare(self):
        self.assertEqual(calculate_taxi_fare(3.5, 0), 50.0)

    def test_calculate_taxi_fare_input_wait_time_10_should_return_55(self):
        self.assertEqual(calculate_taxi_fare(0, 10), 55.0)

    def test_calculate_taxi_fare_input_wait_time_negative_should_raise_value_error(self):
        self.assertRaises(ValueError, calculate_taxi_fare, 0, -5)

    def test_calculate_taxi_fare_input_wait_time_non_integer_should_raise_type_error(self):
        self.assertRaises(TypeError, calculate_taxi_fare, 0, "ten")

    def test_calculate_taxi_fare_input_distance_and_wait_time_should_return_correct_fare(self):
        self.assertEqual(calculate_taxi_fare(5, 10), 79.0)
        self.assertEqual(calculate_taxi_fare(3.5, 5), 60.0)

    def test_calculate_taxi_fare_input_distance_15_should_return_correct_fare(self):
        self.assertEqual(calculate_taxi_fare(15,0), 139.0)


