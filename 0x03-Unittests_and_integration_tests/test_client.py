#!/usr/bin/env python3

"""
This module contains the TestGithubOrgClient class which tests
the GithubOrgClient class from the client module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "mock"})
    def test_org(
        self, org_name: str, expected: Dict, mock_get_json: Mock
    ) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.
        Ensure get_json is called once with the expected argument.
        Args:
            org_name (str): The name of the organization.
            expected (Dict): The expected return value of the org method.
            mock_get_json (Mock): The mocked get_json function.
        """
        client = GithubOrgClient(org_name)
        result = client.org()

        # Check that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Check that the result matches the expected value
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
