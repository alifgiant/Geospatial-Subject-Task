"""
Test Input Reader
"""

import unittest
from input_reader import read_input

class TestInputReader(unittest.TestCase):
    """
    Test Class
    """
    def test_read_input(self):
        data = read_input("test/region-5/region-5.input")
        self.assertEqual(len(list(data)), 4)

        data = read_input("test/region-15/region-15.input")
        self.assertEqual(len(list(data)), 15)

if __name__ == '__main__':
    unittest.main()