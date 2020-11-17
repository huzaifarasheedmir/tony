"""
~~~~~~~~~~~~~~~~~
elt.ml.tony_classifier.py

Classifier class implementation for prediction
~~~~~~~~~~~~~~~~~
"""
import logging
from joblib import load
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from etl.config import EtlConfig

logger = logging.getLogger("ml.tony_classifier")


class TonyClassifier:
    """Implements classifier for sentimental analysis and predict score"""

    model = load(EtlConfig.MODEL_PATH)

    def __init__(self, model=None):
        self.model = model if model else TonyClassifier.model
        self.__sa = SentimentIntensityAnalyzer()

    def load_model(self, path):
        """Load model from provided path"""

        self.model = load(path)

    def __polarity(self, text):
        """Predict the polarity of provide review text"""

        return self.__sa.polarity_scores(text)["compound"]

    def __predict_prob(self, value):
        """Predict the probability of review how much it is positive within 0-1"""

        score = self.model.predict_proba([[value]])[0][1]
        return float("{:.2f}".format(score))

    def predict(self, df):
        """Predict and add score column in dataframe"""

        df["score"] = df["text"].map(self.__polarity).map(self.__predict_prob)
        return df
