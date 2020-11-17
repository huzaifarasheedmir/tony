"""
~~~~~~~~~~~~~~~~~
pipelines.pipeline.py

Implements pipeline for products etl

TonyPipeline accepts any data source or any classifier and it will run
the pipeline covering the provided stages
~~~~~~~~~~~~~~~~~
"""
import logging

from etl.ml.tony_df import TonyDf

logger = logging.getLogger("pipelines.pipeline")


class TonyPipeline:
    """
    Implement stages of Extract Transform and Load using provided Datasource
    """

    def __init__(self, classifier, product_service, source):
        self.__source = source
        self.__classifier = classifier
        self.__prodcut_service = product_service
        self._stages = [self.__extract, self.__transform, self.__load]

    def __extract(self, *args, **kwargs):
        """Extract raw data from data source end point"""

        logger.info("extracting from source . . .")
        return self.__source.pull(*args, **kwargs)

    def __transform(self, product_template):
        """Covert raw data into required template and perform predicitons"""

        logger.info("transforming data . . .")
        product_template = self.__source.to_template(product_template)
        reviews = product_template["reviews"]
        reviews_df = TonyDf(reviews).enrich()
        score_df = self.__classifier.predict(reviews_df)
        product_template["reviews"] = score_df.df_to_dict()
        return product_template

    def __load(self, product_template):
        """Load results in db"""

        logger.info("loading data in db . . .")
        self.__prodcut_service.add_from_template(product_template)
        self.__prodcut_service.aggregate_product_score(
            product_template["source_product_id"]
        )

    def run(self, *args, **kwargs):
        """Execute all the stage in stages array"""

        out = None
        for stage in self._stages:
            if not out:
                out = stage(*args, **kwargs)
                continue
            out = stage(out)
