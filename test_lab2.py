import unittest
from lab2 import binar_search

class TestBinarSearch(unittest.TestCase):
    def test_1(self):
        self.assertEqual(binar_search([3,6,7,11], 8), 4)
    
    def test_2(self):
        self.assertEqual(binar_search([30,11,23,4,20], 5), 30)
    
    def test_3(self):
        self.assertEqual(binar_search([30,11,23,4,20], 6), 23)

if __name__ == '__main__':
    unittest.main()
