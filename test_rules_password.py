import unittest
from rules_password import *

class TestRulesPassword(unittest.TestCase):
    
    def test_min_size(self):
        self.assertEqual(min_size("Alfredo", 7), True)
        self.assertEqual(min_size("Alfredo", 8), False)
    
    def test_min_upper_case(self):
        self.assertEqual(min_upper_case("TesteSenhaForte!123&", 2), True)
        self.assertEqual(min_upper_case("TesteSenhaForte!123&", 10), False)

    def test_min_lower_case(self):
        self.assertEqual(min_lower_case("senHA123", 2), True)
        self.assertEqual(min_lower_case("senHA123", 7), False)

    def test_min_digit(self):
        self.assertEqual(min_digit("python12345", 3), True)
        self.assertEqual(min_digit("python12345", 6), False)

    def test_min_special_chars(self):
        self.assertEqual(min_special_chars("graphQL$!?", 1), True)
        self.assertEqual(min_special_chars("graphQL$!?", 8), False)

    def test_no_repeted(self):
        self.assertEqual(no_repeted("testeteste", 0), True)
        self.assertEqual(no_repeted("teesteteste", 0), False)
        self.assertEqual(no_repeted("teeesteteste", 0), False)

if __name__ == "__main__":
    unittest.main()