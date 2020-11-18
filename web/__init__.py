"""
~~~~~~~~~~~~~~~~~
web.__init__.py

Implements web app creations
~~~~~~~~~~~~~~~~~
"""

from logging.config import dictConfig

from flask import Flask
from flask_mongoengine import MongoEngine

from web.common.exceptions import HttpException
from web.config import WebConfig
from web.handlers import api_error_handler

db = MongoEngine()


def create_app():
    """Create app with using configgit """

    app = Flask(__name__)
    app.config.from_object(WebConfig)

    app.logger.debug("debug")

    db.init_app(app)

    if app.config.get("DEBUG"):
        app.config["LOGGING_CONFIG"]["root"]["level"] = "DEBUG"
    dictConfig(app.config["LOGGING_CONFIG"])

    app.register_error_handler(HttpException, api_error_handler)

    from web.products import products

    app.register_blueprint(products, url_prefix="/v1")

    return app
