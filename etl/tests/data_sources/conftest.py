"""
~~~~~~~~~~~~~~~~~
tests.data_sources.conftest.py

Implements config and fixtures requirements for datasources tests
~~~~~~~~~~~~~~~~~
"""

import pytest
from etl.data_sources.amazon_sources.file_source import AmazonFileSource


@pytest.fixture(scope="module")
def mock_reviews(fixture_loader):
    """
    Mock reviews fixture
    """

    return fixture_loader("mock_reviews")


@pytest.fixture(scope="module")
def mock_template(fixture_loader):
    """
    Mock template fixture
    """

    return fixture_loader("mock_template")


@pytest.fixture(scope="module")
def file_source():
    """
    Amazon file data source
    """
    return AmazonFileSource()
