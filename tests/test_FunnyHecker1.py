from coe_6810110510.Heckerrank1Funny import funnyString
import unittest

#ตามHeckerrank
class FunnyHecker1TestCase(unittest.TestCase):
    def test_funny_string_input_acxz_should_be_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_funny_string_input_bmop_should_be_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")
    
    def test_funny_string_input_ivvkxq_should_be_not_funny(self):
        self.assertEqual(funnyString("ivvkxq"), "Not Funny")

    def test_funny_string_input_ivvkx_should_be_not_funny(self):
        self.assertEqual(funnyString("ivvkx"), "Not Funny")



#เพิ่มเติม
    def test_funny_string_input_a_should_be_funny(self):
        self.assertEqual(funnyString("a"), "Funny")

    def test_funny_string_input_empty_should_be_funny(self):
        self.assertEqual(funnyString(""), "Funny")
