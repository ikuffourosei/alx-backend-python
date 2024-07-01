#!/usr/bin/env python3
'''Test for access_nested_maps'''
from utils import access_nested_map, get_json
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    class TestGetJson(unittest.TestCase):
        """Tests the get_json method from utils.py"""
        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
        def test_get_json(self, test_url, test_payload):
            """Test get_json with a mock url"""
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            with patch('utils.request.get',
                       return_value=mock_response) as mock_request_get:
                results = get_json(test_url)
                mock_request_get.assert_called_once_with(test_url)
                self.assertEqual(results, test_payload)


if __name__ == '__main__':
    unittest.main()
