from .base import ServiceError


class _ErrorCode:
    non = ServiceError(0, 'Success')
    variables_missing = ServiceError(1001, 'Missing environment variables')


error = _ErrorCode()
