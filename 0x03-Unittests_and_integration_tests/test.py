#!/usr/bin/env python3
from parameterized import parameterized, parameterized_class
import unittest
import math

class TestMathUnitTest(unittest.TestCase):
   @parameterized.expand([
       (-1.5, -2.0),
       (1, 1.0),
       (1.6, 1),
   ])
   def test_floor(self, input, expected):
       self.assertEqual(math.floor(input), expected)


if __name__ == "__main__":
    unittest.main()
