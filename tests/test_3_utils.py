from coe_6810110510.n3_utils import is_valid_password
import unittest

class TestIsValidPassword(unittest.TestCase):
    def test_valid_password_input_password43288_should_return_true(self):
        self.assertTrue(is_valid_password("Password43288"))

    def test_short_password_input_Pass5_should_return_false(self):
        self.assertFalse(is_valid_password("Pass5"))

    def test_password_without_uppercase_input_password88778_should_return_false(self):
        self.assertFalse(is_valid_password("password88778"))

    def test_password_without_lowercase_input_PASSWORD4858_should_return_false(self):
        self.assertFalse(is_valid_password("PASSWORD4858"))

    def test_password_without_number_input_Password_should_return_false(self):
        self.assertFalse(is_valid_password("Password"))

    def test_password_with_only_numbers_input_12345678_should_return_false(self):
        self.assertFalse(is_valid_password("12345678"))

    def test_password_with_only_uppercase_input_PASSWORD_should_return_false(self):
        self.assertFalse(is_valid_password("PASSWORD"))
    
    def test_password_with_only_lowercase_input_password_should_return_false(self):
        self.assertFalse(is_valid_password("password"))

    def test_good_password_with_special_characters_should_return_true(self):
        self.assertTrue(is_valid_password("Password177!"))

    def test_password_with_spaces_input_Password_123_should_return_true(self):
        self.assertTrue(is_valid_password("Password 123"))

    def test_password_input_None(self):
        self.assertFalse(is_valid_password(None))
