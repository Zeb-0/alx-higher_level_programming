#!/usr/bin/python3

"""Unittests for max_integer([..])."""



import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains unittests for the max_integer function
    """

    def test_empty_list(self):
        """
        Test the function with an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        """
        Test the function with a list of positive integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 3, 2, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 2, 3, 1]), 5)

    def test_negative_numbers(self):
        """
        Test the function with a list of negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -2, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -2, -3, -1]), -1)

    def test_mixed_numbers(self):
        """
        Test the function with a mix of positive and negative integers
        """
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([-1, -3, 0, 4, -5]), 4)

    def test_float_numbers(self):
        """
        Test the function with a list of float numbers
        """
        self.assertEqual(max_integer([1.0, 2.5, 3.7, 4.2]), 4.2)
        self.assertEqual(max_integer([4.2, 3.7, 2.5, 1.0]), 4.2)
        self.assertEqual(max_integer([1.0, 3.7, 2.5, 4.2]), 4.2)

    def test_strings(self):
        """
        Test the function with a list of strings
        """
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')
        self.assertEqual(max_integer(['dog', 'cat', 'bird']), 'dog')
        self.assertEqual(max_integer(['chair', 'table', 'lamp']), 'table')

    def test_mixed_types(self):
        """
        Test the function with a mix of different data types
        """
        with self.assertRaises(TypeError):
            max_integer([1, 'apple', 3.7, -4, 5])

if __name__ == '__main__':
    unittest.main()
