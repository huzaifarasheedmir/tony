"""
~~~~~~~~~~~~~~~~~
tests.datasources.test_amazon_file_source.py

Implements amazon file datasource tests
~~~~~~~~~~~~~~~~~
"""
from etl.config import TestingConfig
from etl.data_sources.amazon_sources.file_source import AmazonFileSource


def test_file_source_pull(file_source: AmazonFileSource, mock_reviews):
    """
    Test whether data source reads provided file
    """
    assert (
        file_source.pull(
            file_path="{}mock_reviews.json".format(TestingConfig.FIXTURES_DIR)
        )
        == mock_reviews
    )


def test_file_source_to_template(
    file_source: AmazonFileSource, mock_reviews, mock_template
):
    """
  Test whether data source converts raw reviews to required templates
  """
    assert file_source.to_template(mock_reviews) == mock_template
