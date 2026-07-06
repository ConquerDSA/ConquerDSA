import httpx

from conquerdsa.exceptions.service import ServiceUnavailableError
from conquerdsa.services.base import BaseHTTPClient


class GitHubService(BaseHTTPClient):
    BASE_URL = "https://api.github.com"

    @classmethod
    def validate_username(cls, username: str) -> bool:
        try:
            with cls() as github:
                response = github.get(
                    f"{cls.BASE_URL}/users/{username}"
                )

            if response.status_code == 200:
                return True

            if response.status_code == 404:
                return False

            raise ServiceUnavailableError(
                f"GitHub returned status code {response.status_code}"
            )

        except httpx.HTTPError as e:
            raise ServiceUnavailableError(
                "Unable to connect to GitHub."
            ) from e