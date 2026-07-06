import httpx


class BaseHTTPClient:
    """Base HTTP client for external services."""

    TIMEOUT = 10

    def __init__(self) -> None:
        self._client = httpx.Client(
            timeout=self.TIMEOUT,
            headers={
                "User-Agent": "ConquerDSA/0.1.0",
            },
        )

    def get(self, *args, **kwargs):
        return self._client.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self._client.post(*args, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()