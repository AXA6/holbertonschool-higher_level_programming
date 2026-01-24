#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_max_at_beginning(self):
        """Test list where max is at the beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test list where max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-3, -1, -5, -2]), -1)

    def test_mixed_int_float(self):
        """Test list with mixed ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.9]), 3)

    def test_strings(self):
        """Test list with strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_list_of_lists(self):
        """Test list of lists (comparison by first element)"""
        self.assertEqual(max_integer([[1, 2], [3, 4], [0, 5]]), [3, 4])

    def test_none_value(self):
        """Test list containing None should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_non_list_argument(self):
        """Test passing a non-list argument should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == "__main__":
    unittest.main()
