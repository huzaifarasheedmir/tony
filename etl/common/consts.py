"""
~~~~~~~~~~~~~~~~~
common.consts.py

Contains constants which are available to all modules in etl service
~~~~~~~~~~~~~~~~~
"""

from etl.data_sources.amazon_sources.file_source import AmazonFileSource

AMAZON_SOURCE_MAPPER = {
    "file": AmazonFileSource
}  # Source mapper if different kind of amazon sources, Rgister all new amazon sources here
