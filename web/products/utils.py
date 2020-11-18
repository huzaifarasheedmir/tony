"""
~~~~~~~~~~~~~~~~~
web.products.utils.py

Park all products utils here
~~~~~~~~~~~~~~~~~
"""

import logging
from web.common.utils import oid_to_str, get_offset_and_limit
from web.config import WebConfig

logger = logging.getLogger("products.api")


def parse_products_response(category, text, page_num, product_service):
    total = (
        product_service.products.objects(category=category).search_text(text).count()
    )
    if total == 0:
        return
    offset, limit = get_offset_and_limit(page_num=page_num)
    products = (
        product_service.products.objects(category=category)
        .search_text(text)
        .order_by("-rating_score")[offset:limit]
        .as_pymongo()
    )
    products = list(map(lambda product: oid_to_str(product), products))
    response = {
        "products": products,
        "response_meta": {
            "total_records": total,
            "current_page": page_num,
            "records_per_page": WebConfig.PAGE_SIZE,
        },
    }
    if total >= WebConfig.PAGE_SIZE:
        response["response_meta"][
            "next_page"
        ] = "{}/v1/products?category={}&&text={}&&page={}".format(
            WebConfig.HOST, category, text, page_num + 1
        )
    if page_num == 1:
        response["products"] = products[1:]
        response["recommended_product"] = products[0]

    return response
