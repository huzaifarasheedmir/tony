"""
~~~~~~~~~~~~~~~~~
data_sources.amazon.file_source.py

Implements amazon data source for json files
~~~~~~~~~~~~~~~~~
"""

import json
import logging
import os

from etl.common.exceptions import PipelineBroken
from etl.data_sources.base_source import BaseDataSource

logger = logging.getLogger("amazon_sources.file_source")


class AmazonFileSource(BaseDataSource):
    """
    Implement functionality for all datasources
    """

    NAME = "AMAZON"
    _ERROR_DIR_NOT_FOUND = "{} dir not exists."
    _ERROR_INVALID_JSON = "{} key is not in payload"
    field_mapper = {
        "date": "reviews.date",
        "source_review_id": "reviews.id",
        "rating": "reviews.rating",
        "text": "reviews.text",
        "source_product_id": "id",
        "asin": "asins",
        "category": "primaryCategories",
        "sub_categories": "categories",
        "added_at": "dateAdded",
        "manufacturer": "manufacturer",
    }
    required_product_fields = {
        "id",
        "dateAdded",
        "name",
        "asins",
        "brand",
        "categories",
        "primaryCategories",
        "manufacturer",
        "reviews",
    }
    required_review_fields = {
        "reviews.date",
        "reviews.id",
        "reviews.rating",
        "reviews.text",
    }

    def pull(self, *args, **kwargs):
        """
        Pull product from data source
        """
        file_path = kwargs.get("file_path")
        if not file_path:
            raise PipelineBroken("file_path arg is required")
        try:
            with open(file_path) as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            logger.error(str(e))
            raise PipelineBroken(str(e))

    def batch_pull(self, *args, **kwargs):
        """
        Pull all files in dir and run pipeline for each file
        """
        from etl.tasks.amazon_tasks import run_amazon_pipeline

        products_dir = kwargs.get("products_dir")
        if not products_dir or not os.path.isdir(products_dir):
            message = AmazonFileSource._ERROR_DIR_NOT_FOUND.format(products_dir)
            logger.error(message)
            raise PipelineBroken(message)

        for file in os.listdir(products_dir):
            if file.endswith(".json"):
                run_amazon_pipeline.delay(
                    source_type="file", file_path="{}/{}".format(products_dir, file)
                )

    def to_template(self, raw_data):
        """
        Convert the file json to prodcut template
        """
        field_mapper = AmazonFileSource.field_mapper
        try:
            return {
                "source_product_id": raw_data[field_mapper["source_product_id"]],
                "category": raw_data[field_mapper["category"]],
                "added_at": raw_data[field_mapper["added_at"]],
                "asin": raw_data[field_mapper["asin"]],
                "sub_categories": raw_data[field_mapper["sub_categories"]],
                "manufacturer": raw_data[field_mapper["manufacturer"]],
                "name": raw_data["name"],
                "brand": raw_data["brand"],
                "source": AmazonFileSource.NAME,
                "reviews": [
                    {
                        "date": review[field_mapper["date"]],
                        "source_review_id": review[field_mapper["source_review_id"]],
                        "rating": review[field_mapper["rating"]],
                        "text": review[field_mapper["text"]],
                    }
                    for review in raw_data["reviews"]
                ],
            }
        except KeyError as e:
            message = AmazonFileSource._ERROR_INVALID_JSON.format(str(e))
            logger.error(message)
            raise PipelineBroken(message)
