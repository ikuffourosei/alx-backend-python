#!/usr/bin/env python3
'''Test for access_nested_maps'''
from utils import access_nested_map
from parameterized import parameterized
import unittest
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map from utils.py"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, outcome):
        self.assertEqual(access_nested_map(nested_map, path), outcome)


if __name__ == '__main__':
    unittest.main()
