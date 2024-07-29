#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict
import requests
from functools import wraps
from typing import Callable
from utils import access_nested_map, get_json, memoize

"""
    Module for class TestAccessNestedMap that
    inherits from unittest.TestCase. And test
    utils.access_nested_map.
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
           Test that accessing a nested map with an invalid path
           raises KeyError.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test suite for the get_json function from utils."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get):
        """
            In this function we are going to :
            -Test that get_json returns the expected result.
            -Set up the mock to return a response with the test_payload
            -Call the function with the test_url
            -Assert the mocked get method was called once with the test_url
            -Assert that the result is equal to the test_payload
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """Class to demonstrate memoization."""
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    in the codes below we will have:
        -Test suite for the memoize decorator.
        -This converts a_property into a property that caches its result.
        -Test that memoize correctly caches results.
        -Create an instance of TestClass
        -Call a_property twice
        -Assertions
    """

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        obj = TestClass()
        result_first_call = obj.a_property
        result_second_call = obj.a_property
        self.assertEqual(result_first_call, 42)
        self.assertEqual(result_second_call, 42)
        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
