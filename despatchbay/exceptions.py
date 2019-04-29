"""Despatchbay SDK exceptions"""


class Error(Exception):
    """Base class for other exceptions"""


class InvalidArgumentException(Error):
    """Exception to raise when invalid arguments are passed."""


class AuthorizationException(Error):
    """Exception to raise when a 401 error is returned."""


class PaymentException(Error):
    """Exception to raise when an operation fails due to insufficient funds."""


class ApiException(Error):
    """General API exception"""


class ConnectionException(Error):
    """General connection error exception."""


class RateLimitException(Error):
    """Exception to raise when an operation fails due rate limits."""
