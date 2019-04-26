class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidArgumentException(Error):
    pass


class AuthorizationException(Error):
    pass


class PaymentException(Error):
    pass


class ApiException(Error):
    pass


class ConnectionException(Error):
    pass


class RateLimitException(Error):
    pass