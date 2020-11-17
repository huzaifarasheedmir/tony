"""
~~~~~~~~~~~~~~~~~
common.exceptions.py

Contains exceptions which are available to all modules in etl service
~~~~~~~~~~~~~~~~~
"""


class PipelineBroken(Exception):
    """ Exception raised when an error occurs in pipeline processing"""

    def __init__(self, error):
        self.msg = error
        super(PipelineBroken, self).__init__(self.msg)
