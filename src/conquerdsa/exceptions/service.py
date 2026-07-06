class ServiceError(Exception):
    """Base exception for external services."""


class ServiceUnavailableError(ServiceError):
    """Raised when an external service is unavailable."""