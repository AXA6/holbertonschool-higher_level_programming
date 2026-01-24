#!/usr/bin/python3
import unittest
max_int = __import__('6-max_integer').max_integer
class TestMax(unittest.TestCase):    
    def test_Max(self):
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([13, 14, 56, 565]), 565)
        self.assertEqual(max_int([-1]), -1)
        self.assertEqual(max_int([555, 454 ,7]), 555)
        self.assertEqual(max_int([555, 654 ,7]), 654)
        self.assertEqual(max_int([555, -1 ,7]), 555)
        self.assertEqual(max_int([7]), 7)
        with self.assertRaises(TypeError):
            max_int(["er", 56, 556])
