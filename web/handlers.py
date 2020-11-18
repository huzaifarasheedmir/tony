"""
~~~~~~~~~~~~~~~~~
web.handlers.py

Implements handler for apis errors
~~~~~~~~~~~~~~~~~
"""

import logging

from flask import jsonify


logger = logging.getLogger("web.handlers")


def api_error_handler(e):
    """Handle all exceptions and generate corresponding response"""
    message = str(e)
    if len(message) > 0:
        message = message[0].upper() + message[1:]
        message = "{}.".format(message) if message[-1] != "." else message
    return jsonify({"message": message}), e.status
