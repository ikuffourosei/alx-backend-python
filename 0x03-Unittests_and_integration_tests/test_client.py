#!/usr/bin/env python3
"""Test cases for GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, orgname, mock_get_json):
        """Test org method of GithubOrgClient"""

        mock_response = {'login': orgname, 'id': 12345, 'node_id': 'abc123'}
        mock_get_json.return_value = mock_response

        git = GithubOrgClient(orgname)

        result = git.org
        self.assertEqual(result, mock_response)

        mock_get_json.assert_called_once_with(git.ORG_URL.format(org=orgname))


if __name__ == '__main__':
    unittest.main()
