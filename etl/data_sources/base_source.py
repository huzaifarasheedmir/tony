"""
~~~~~~~~~~~~~~~~~
data_sources.base_source.py

Implements base data source
~~~~~~~~~~~~~~~~~
"""


class BaseDataSource:
    """
    Implement functionality for all datasources
    """

    NAME = ""

    def pull(self, *args, **kwargs):
        """
        Pull product data from data source
        """
        pass

    def batch_pull(self, *args, **kwargs):
        """
        Pull product data in batches from source
        """
        pass

    def to_template(self, *args, raw_data):
        """
        Convert the file json to prodcut template
        """
        pass
