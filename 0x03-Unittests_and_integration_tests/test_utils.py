#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Adjust the import based on your project structure

"""
    Module for class TestAccessNestedMap that
     inherits from unittest.TestCase. And test
     utils.access_nested_map
"""

class TestAccessNestedMap(unittest.TestCase):
    """
        A class to implement the TestAccessNestedMap.
        test_access_nested_map method to test that the method
        returns what it is supposed to.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
            Test the access_nested_map function for different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()