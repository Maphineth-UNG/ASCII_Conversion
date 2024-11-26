"""
Unit tests for ASCII conversion functions in main.py.
Tests the functionality of:
1. ascii_to_binary
2. ascii_to_decimal
3. ascii_to_hexadecimal
"""
import unittest
from main import ascii_to_binary, ascii_to_decimal, ascii_to_hexadecimal
class TestAsciiConversion(unittest.TestCase):
    """Test suite for ASCII conversion functions."""
    def test_ascii_to_binary(self):
        """Test binary conversion of ASCII text."""
        self.assertEqual(ascii_to_binary("A"), "01000001")
        self.assertEqual(ascii_to_binary("AB"), "01000001 01000010")
        self.assertEqual(ascii_to_binary(" "), "00100000")
        self.assertEqual(ascii_to_binary("!"), "00100001")
    def test_ascii_to_decimal(self):
        """Test decimal conversion of ASCII text."""
        self.assertEqual(ascii_to_decimal("A"), "65")
        self.assertEqual(ascii_to_decimal("AB"), "65 66")
        self.assertEqual(ascii_to_decimal(" "), "32")
        self.assertEqual(ascii_to_decimal("!"), "33")
    def test_ascii_to_hexadecimal(self):
        """Test hexadecimal conversion of ASCII text."""
        self.assertEqual(ascii_to_hexadecimal("A"), "41")
        self.assertEqual(ascii_to_hexadecimal("AB"), "41 42")
        self.assertEqual(ascii_to_hexadecimal(" "), "20")
        self.assertEqual(ascii_to_hexadecimal("!"), "21")
    def test_empty_input(self):
        """Test conversion of empty ASCII text."""
        self.assertEqual(ascii_to_binary(""), "")
        self.assertEqual(ascii_to_decimal(""), "")
        self.assertEqual(ascii_to_hexadecimal(""), "")
if __name__ == '__main__':
    unittest.main()
