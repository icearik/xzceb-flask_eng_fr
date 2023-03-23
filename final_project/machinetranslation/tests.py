"""My simple tester"""
import unittest
from translator import egnlish_to_french, french_to_english

class MyTester(unittest.TestCase):
    """Test class"""

    def test_e2f(self):
        """Matching translation"""
        self.assertEqual(egnlish_to_french('Hello'), 'Bonjour')

    def test_e2f_ne(self):
        """""Mismatching translation"""
        self.assertNotEqual(egnlish_to_french('Bye'), 'Bonjour')

    def test_e2f_null(self):
        """Null inp"""
        with self.assertRaises(ValueError):
            egnlish_to_french(None)

    def test_f2e(self):
        """""Matching translation"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_f2e_ne(self):
        """""Mismatching translation"""
        self.assertNotEqual(french_to_english('Bonjour'), 'Bye')

    def test_f2e_null(self):
        """Null inp"""
        with self.assertRaises(ValueError):
            french_to_english(None)

if __name__ == '__main__':
    unittest.main()
