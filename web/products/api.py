"""
~~~~~~~~~~~~~~~~~
web.products.api.py

Park all products apis here
~~~~~~~~~~~~~~~~~
"""

import logging


from flask import jsonify, request, Response
from dao.product_service import ProductService
from web.products.utils import parse_products_response
from web.common.exceptions import BadRequest
from web.products import products

logger = logging.getLogger("products.api")

product_service = ProductService()


@products.route("/products/categories", methods=["GET"])
def get_categories():
    """Get categories"""
    categories = product_service.list_categories()
    if not categories:
        return Response(status=204)

    return jsonify({"categories": categories}), 200


@products.route("/products", methods=["GET"])
def search_products():
    """Search products"""

    category = request.args.get("category")
    if not category:
        raise BadRequest("Product category is required in args")
    text = request.args.get("text")
    if not text:
        raise BadRequest("Product text is required in args")

    page_num = int(request.args.get("page", "1"))
    response = parse_products_response(
        category=category, text=text, page_num=page_num, product_service=product_service
    )
    if not response:
        raise Response(status=204)

    return jsonify(response), 200
