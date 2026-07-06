import httpx

from conquerdsa.exceptions.service import ServiceUnavailableError
from conquerdsa.graphql.queries import VALIDATE_LEETCODE_USER
from conquerdsa.services.base import BaseHTTPClient


class LeetCodeService(BaseHTTPClient):
    BASE_URL = "https://leetcode.com/graphql"

    @classmethod
    def validate_username(cls, username: str) -> bool:
        payload = {
            "query": VALIDATE_LEETCODE_USER,
            "variables": {
                "username": username,
            },
            "operationName": "userPublicProfile",
        }

        try:
            with cls() as leetcode:
                response = leetcode.post(cls.BASE_URL, json=payload)

            if response.status_code != 200:
                raise ServiceUnavailableError(
                    f"LeetCode returned status code {response.status_code}"
                )

            data = response.json()
            

            return data["data"]["matchedUser"] is not None

        except httpx.HTTPError as e:
            raise ServiceUnavailableError(
                "Unable to connect to LeetCode."
            ) from e