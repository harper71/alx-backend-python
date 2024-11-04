#!/usr/bin/env python3
"""unittest on the access_nested_map function"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Callable, Sequence, Any


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
