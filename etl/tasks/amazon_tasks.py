"""
~~~~~~~~~~~~~~~~~
etl.tasks.amazon_tasks.py

Implements task for scalable, distributed, parallel execution
~~~~~~~~~~~~~~~~~
"""
import logging
from etl.celery_app import celery_app
from etl.data_sources.amazon_sources.file_source import AmazonFileSource
from dao.product_service import ProductService
from etl.ml.tony_classifier import TonyClassifier
from etl.pipelines.tony_pipeline import TonyPipeline
from etl.common.consts import AMAZON_SOURCE_MAPPER

logger = logging.getLogger("tasks.amazon_tasks")


@celery_app.task(name="amazon_batch_executor", queue="amazon_tasks_queue")
def run_amazon_batch_pipeline(*args, source_type, **kwargs):
    """Run pipeline for batches of data"""

    source_class = AMAZON_SOURCE_MAPPER.get(source_type, AmazonFileSource)
    source = source_class()
    source.batch_pull(*args, **kwargs)


@celery_app.task(name="amazon_solo_executor", queue="amazon_tasks_queue")
def run_amazon_pipeline(*args, source_type, **kwargs):
    """Run pipeline for single batch data"""

    source_class = AMAZON_SOURCE_MAPPER.get(source_type, AmazonFileSource)
    source = source_class()
    product_service = ProductService()
    classifier = TonyClassifier()
    pipeline = TonyPipeline(
        classifier=classifier, product_service=product_service, source=source
    )
    pipeline.run(*args, **kwargs)
