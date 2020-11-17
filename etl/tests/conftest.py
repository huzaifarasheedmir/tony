"""
~~~~~~~~~~~~~~~~~
tests.conftest.py

Implements config and fixtures foll all etl service tests
~~~~~~~~~~~~~~~~~
"""

import pytest
from etl.config import TestingConfig
import yaml


@pytest.fixture(scope="session")
def fixture_loader():
    """
    Load mock fixture files
    """
    return load_fixture


def load_fixture(name):
    """
    Read yml file
    """
    with open("{}{}.yml".format(TestingConfig.FIXTURES_DIR, name), "r") as f:
        return yaml.full_load(f)
