"""
~~~~~~~~~~~~~~~~~
elt.config.py

Implements the configurations for diff elements of the app
~~~~~~~~~~~~~~~~~
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DatabaseConfig:
    """Db configs"""

    MONGO_DB_PARAMS = {
        "USER": os.environ.get("MONGODB_MONGO_USER", "admin"),
        "PASSWORD": os.environ.get("MONGODB_MONGO_PASSWORD", "password"),
        "HOST": os.environ.get("MONGODB_MONGO_HOST", "172.17.0.1"),
        "PORT": os.environ.get("MONGODB_MONGO_USER", "27017"),
        "DB": os.environ.get("MONGODB_MONGO_DB", "tonydb"),
    }
    MONGO_DB_URL = (
        "mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?authSource={DB}"
        "&authMechanism=DEFAULT".format(**MONGO_DB_PARAMS)
    )


class RabbitMQConfig:
    """Rabbitmq configs"""

    RABBIT_PARAMS = {
        "RABBIT_ENV_RABBITMQ_USER": os.environ.get("RABBIT_ENV_RABBITMQ_USER", "guest"),
        "RABBIT_ENV_RABBITMQ_PASSWORD": os.environ.get(
            "RABBIT_ENV_RABBITMQ_PASSWORD", "guest"
        ),
    }
    RABBIT_URL = "amqp://{RABBIT_ENV_RABBITMQ_USER}:{RABBIT_ENV_RABBITMQ_PASSWORD}@rabbitmq:5672//".format(
        **RABBIT_PARAMS
    )


class EtlConfig:
    """Config for ETL service"""

    FIRE_INTERVAL = float(
        os.environ.get("ETL_INTERVAL", "60.0")
    )  # After how much interval etl execute
    MODEL_PATH = os.environ.get(
        "MODEL_PATH", "classifier_model.joblib"
    )  # can pull from S3
    SAMPLE_FILES_DIR = os.environ.get(
        "FILES_DIR", "sample_products/"
    )  # can pull from S3
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(name)s [%(lineno)s]: %(message)s"
            }
        },
        "root": {"level": "INFO", "handlers": ["console"]},
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
    }


class TestingConfig:
    """
    Config for testing environment
    """

    FIXTURES_DIR = os.path.join(BASE_DIR, "tests/fixtures/")
