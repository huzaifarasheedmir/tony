from flask import Blueprint

products = Blueprint("products", __name__)

from web.products import api
