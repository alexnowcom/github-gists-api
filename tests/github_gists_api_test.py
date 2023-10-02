import unittest
import requests

class TestGitHubGistsAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8080"  # Adjust the URL if your API runs on a different address

    def test_get_user_gists_valid_user(self):
        username = "octocat"  # Replace with a valid GitHub username
        response = requests.get(f"{self.BASE_URL}/{username}")

        self.assertEqual(response.status_code, 200)
        gists = response.json()
        self.assertTrue(isinstance(gists, list))

    def test_get_user_gists_invalid_user(self):
        username = "nonexistentuser"  # Replace with a nonexistent GitHub username
        response = requests.get(f"{self.BASE_URL}/{username}")

        self.assertEqual(response.status_code, 404)
        error_message = response.json().get("error")
        self.assertEqual(error_message, "User not found")

if __name__ == "__main__":
    unittest.main()
