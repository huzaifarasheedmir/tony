"""
~~~~~~~~~~~~~~~~~
web.common.exceptions.py

Custom exceptions to raise according to response
~~~~~~~~~~~~~~~~~
"""


class HttpException(Exception):
    status = None


class BadRequest(HttpException):
    """Raised when payload is invalid"""

    status = 400

    def __init__(self, msg="Invalid payload"):
        self.args = (msg,)
