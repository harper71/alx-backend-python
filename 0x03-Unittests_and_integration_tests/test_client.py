#!/usr/bin/env python3
"""test for client module"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient, get_json
from parameterized import parameterized
from typing import Dict, Any, List

public_repos_fixture = [
    {"name": "repo1", "license": {"key": "mit"}},
    {"name": "repo2", "license": {"key": "apache-2.0"}},
    {"name": "repo3", "license": {"key": "apache-2.0"}},
    {"name": "repo4", "license": {"key": "gpl-3.0"}}
]


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos
        returns the expected list of repo names."""
        # Mock URL and JSON response
        test_url = "https://api.github.com/orgs/test_org/repos"
        mock_public_repos_url.return_value = test_url
        mock_get_json.return_value = public_repos_fixture

        # Initialize the client and call public_repos
        client = GithubOrgClient("test_org")
        result = client.public_repos()

        # Extract expected repo names from the fixture
        expected = [repo["name"] for repo in public_repos_fixture]
        self.assertEqual(result, expected)

        # Verify that _public_repos_url and get_json were called
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(test_url)

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos_with_license(self,
                                       mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos with license filtering."""
        # Mock URL and JSON response
        test_url = "https://api.github.com/orgs/test_org/repos"
        mock_public_repos_url.return_value = test_url
        mock_get_json.return_value = public_repos_fixture

        # Initialize the client and filter by "apache-2.0" license
        client = GithubOrgClient("test_org")
        result = client.public_repos(license="apache-2.0")

        # Extract expected repo names with "apache-2.0" license
        expected = [repo["name"] for repo in public_repos_fixture
                    if repo["license"]["key"] == "apache-2.0"]
        self.assertEqual(result, expected)

        # Verify that _public_repos_url and get_json were called
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json):
        """Test GithubOrgClient.org method with parameterized org names."""

        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"login": org_name})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url
        returns the expected URL."""

        # Define a known payload with a
        # "repos_url" field
        mocked_org_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
            }

        # Patch the org property of GithubOrgClient
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock,
                          return_value=mocked_org_payload):
            # Initialize the client with a test org name
            client = GithubOrgClient("test_org")

            # Call _public_repos_url and verify the result
            result = client._public_repos_url
            self.assertEqual(result, mocked_org_payload["repos_url"])
