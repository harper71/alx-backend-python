#!/usr/bin/env python3
"""unittest on the access_nested_map function"""
import unittest
from unittest.mock import patch, Mock
from typing import Dict, Any, List, Tuple
import unittest.mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {'b': 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nestedMap,
                                         path, exception) -> None:
        """checks the error of the function access_nested_map"""
        with self.assertRaises(exception):
            access_nested_map(nestedMap, path)


class TestGetJson(unittest.TestCase):
    """Test case for the utils.get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, Any], mock_get: Mock) -> None:
        """
        Test the utils.get_json function to
        ensure it returns the expected result.

        This test checks that utils.get_json correctly
        retrieves JSON data from a given URL,
        without making any actual HTTP requests.
        It uses unittest.mock.patch to mock
        requests.get, returning a Mock object with a specified JSON payload.

        Args:
            mock_get (Mock): The mocked requests.get method.

        Test Cases:
            - For the URL "http://example.com",
            the JSON payload should be {"payload": True}.
            - For the URL "http://holberton.io",
            the JSON payload should be {"payload": False}.

        Assertions:
            - Checks that requests.
            get is called exactly once with the correct URL.
            - Ensures the output of utils.
            get_json matches the expected payload.
        """

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set the mock to return our mock response
        mock_get.return_value = mock_response

        # Call the function and store the result
        result: Dict[str, Any] = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """this test the memorize function in util.py"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with unittest.mock.patch.object(TestClass, "a_method",
                                        return_value=42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
