"""
~~~~~~~~~~~~~~~~~
models.utils.py

Park db_related utils here
~~~~~~~~~~~~~~~~~
"""

import logging
from functools import wraps

from mongoengine.errors import NotUniqueError, BulkWriteError

logger = logging.getLogger("models.utils")


def catch_mongo_exceptions(func):
    """Catch mongos exception here"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (NotUniqueError, BulkWriteError) as e:
            pass  # duplication may occur frequently so ignore such errors

    return decorated_function
