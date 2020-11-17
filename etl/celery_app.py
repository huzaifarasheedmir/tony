"""
~~~~~~~~~~~~~~~~~
elt.celery_app.py

Create the app using provided configuration
~~~~~~~~~~~~~~~~~
"""

from celery import Celery
from celery.signals import celeryd_init, worker_shutdown, setup_logging
from mongoengine import connect, disconnect
from logging.config import dictConfig
import nltk

from etl.config import RabbitMQConfig, EtlConfig, DatabaseConfig

celery_app = Celery(
    "tony_etl", broker=RabbitMQConfig.RABBIT_URL, include=["etl.tasks.amazon_tasks"],
)


@celeryd_init.connect()
def worker_init(*args, **kwargs):
    """Runs when a celery worker starts"""

    # Eventually you can download json files form S3 here when a worker starts
    nltk.download("vader_lexicon")
    connect(host=DatabaseConfig.MONGO_DB_URL)


@worker_shutdown.connect()
def worker_shutdown(*args, **kwargs):
    """Runs when a celery worker is shutting down"""

    disconnect()


@setup_logging.connect
def config_loggers(*args, **kwags):
    """
    Setup custom logging config
    """

    dictConfig(EtlConfig.LOGGING_CONFIG)


celery_app.conf.beat_schedule = {
    "run_batch_pipeline": {
        "task": "amazon_batch_executor",
        "schedule": EtlConfig.FIRE_INTERVAL,
        "kwargs": {"source_type": "file", "products_dir": EtlConfig.SAMPLE_FILES_DIR},
    }
}  # Scheduled cron tasks here same task can be run for diff data source by providing the data source type
