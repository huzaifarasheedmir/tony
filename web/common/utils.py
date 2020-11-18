"""
~~~~~~~~~~~~~~~~~
web.common.utils.py

Park all utils functions here which are available through web service
~~~~~~~~~~~~~~~~~
"""
import logging
from web.config import WebConfig

logger = logging.getLogger("web.common.utils")


def oid_to_str(element):
    """Convert mongo oid to str"""

    element["id"] = str(element["_id"])
    del element["_id"]
    return element


def get_offset_and_limit(page_num, page_size=WebConfig.PAGE_SIZE):
    """Get net page offset and limits"""

    page_size = page_size - 1
    offset = (page_num - 1) * page_size
    limit = offset + page_size - 1
    return offset, limit
