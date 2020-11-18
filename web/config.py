"""
~~~~~~~~~~~~~~~~~
web.config.py

Implements the configurations for diff elements of the app
~~~~~~~~~~~~~~~~~
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DatabaseConfig:
    """Db configs"""

    # flask mongo accepts this style of mongo configs
    MONGODB_SETTINGS = {
        "host": os.environ.get("MONGO_HOST") or "mongodb",
        "port": os.environ.get("MONGO_PORT") or 27017,
        "username": os.environ.get("MONGO_USER") or "admin",
        "password": os.environ.get("MONGO_PASSWORD") or "password",
        "db": os.environ.get("MONGO_DB") or "tonydb",
    }


class WebConfig(DatabaseConfig):
    PORT = 8081
    HOST = os.environ.get("HOST", "http://localhost:8081")
    DEBUG = False
    PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "10"))
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(name)s [%(lineno)s]: %(message)s"
            }
        },
        "root": {"level": "INFO", "handlers": ["gunicorn"]},
        "handlers": {
            "gunicorn": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
    }


class TestingConfig:
    FIXTURES_DIR = os.path.join(BASE_DIR, "tests/fixtures")
