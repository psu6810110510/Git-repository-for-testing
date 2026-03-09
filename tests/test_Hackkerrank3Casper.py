from coe_6810110510.Hackerrank3_caesar_cipher import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):

    def test_normal_string_shift_should_be_correct(self):
        self.assertEqual(caesarCipher("abc", 2), "cde")
        self.assertEqual(caesarCipher("ABC", 2), "CDE")

    def test_wrap_around_z_should_be_a(self):
        self.assertEqual(caesarCipher("xyz", 3), "abc")
        self.assertEqual(caesarCipher("VWXYZ", 5), "ABCDE")
        

    def test_special_characters_should_be_unchanged(self):
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(caesarCipher("123-456", 10), "123-456")
        

    def test_large_k_value_should_be_modulo_26(self):
        self.assertEqual(caesarCipher("abc", 28), "cde")
        self.assertEqual(caesarCipher("Hackerrank", 26), "Hackerrank")
