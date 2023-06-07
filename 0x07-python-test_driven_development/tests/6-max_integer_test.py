#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        test_list = [1, 2, 3, 5]
        test_list_2 = [100, 10, 1]
        self.assertEqual(5,max_integer(test_list))
        self.assertEqual(100, max_integer(test_list_2))
    
    def test_type(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "hello"])
        self.assertRaises(TypeError, max_integer, [1, 2, [1,3]])
    def test_negative_max(self):
        test_list = [-1, 5, 8, -1000]
        self.assertEqual(8, max_integer(test_list))
        self.assertEqual(0, max_integer([0, -1]))
    def test_empty(self):
        self.assertEqual(None, max_integer([]))
    def test_infinity(self):
        positive_inf = float('inf')
        negative_inf = float('-inf')
        self.assertEqual(positive_inf, max_integer([1000, positive_inf]))
        self.assertEqual(0, max_integer([0, negative_inf]))
    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        list = [3, 4.5, 2]
        result = max_integer(list)
        self.assertEqual(result, 4.5)
    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        list = [45]
        result = max_integer(list)
        self.assertEqual(result, 45)
    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        list = [8, 8, 8, 8, 8]
        result = max_integer(list)
        self.assertEqual(result, 8)
    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)
if __name__== '__main__':
    unittest.main()
    
