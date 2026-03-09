import unittest
from unittest.mock import patch
from coe_6810110510.Stub import guess_int
from coe_6810110510.Stub import guess_float

class TestGuessNumber(unittest.TestCase):
    @patch('coe_6810110510.Stub.random.randint')
    def test_guess_int_should_return_stubbed_value(self, mock_randint):
        mock_randint.return_value = 5 
        start, stop = 1, 10
        
        result = guess_int(start, stop)
        self.assertEqual(result, 5) 


    @patch('coe_6810110510.Stub.random.uniform')
    def test_guess_float_should_return_stubbed_value(self, mock_uniform):
        mock_uniform.return_value = 5.0
        start, stop = 1.0, 10.0

        result = guess_float(start, stop)
        self.assertEqual(result, 5.0)
