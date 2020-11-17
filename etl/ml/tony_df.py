"""
~~~~~~~~~~~~~~~~~
elt.ml.tony_df.py

Provides custom Dataframe implementation
Our Machine learning classifier only understands a specific form data representation
TonyDf is that presentation of data
~~~~~~~~~~~~~~~~~
"""
import logging
from pandas import DataFrame

logger = logging.getLogger("ml.tony_df")


class TonyDf(DataFrame):
    """Implement customized pandas Dataframe """

    def __init__(self, *args, **kwargs):
        super(TonyDf, self).__init__(*args, **kwargs)

    def df_to_dict(self):
        """Convert rows to dict after select required columns"""

        return self[["source_review_id", "rating", "score"]].to_dict("records")

    def rating_label(self, rating):
        """Assign labels to rating"""

        return 1 if rating >= 4 else 0

    def enrich(self):
        """Add more features in data for ml analysis and prediciton"""

        filtered_df = TonyDf(self[self["rating"] != 3])
        filtered_df["label"] = filtered_df["rating"].map(self.rating_label)
        return filtered_df
