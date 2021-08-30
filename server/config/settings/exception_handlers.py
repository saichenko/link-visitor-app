from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc: Exception, context: dict) -> Response:
    """Custom exception handler for DRF for replacing `detail` on `status.`"""
    response = exception_handler(exc, context)
    response.data.pop('detail', None)
    response.data['status'] = exc.detail

    return response
