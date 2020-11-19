"""
~~~~~~~~~~~~~~~~~
elt.ml.tony_trainer.py

Implements model training
~~~~~~~~~~~~~~~~~
"""

import pandas as pd
from joblib import dump
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# #nltk.download('vader_lexicon')


sid = SentimentIntensityAnalyzer()


def rating_label(rating):
    """Assign labels to ratings"""

    return 1 if rating >= 4 else 0


def calculate_polarity(text):
    """Calculate text sentiment score"""

    return sid.polarity_scores(text)["compound"]


review_cols = ["reviews.rating", "reviews.text"]
data = pd.read_csv("sample.csv")
data = data[data["reviews.rating"] != 3][review_cols]
data["label"] = data["reviews.rating"].map(rating_label)
data["polarity"] = data["reviews.text"].map(calculate_polarity)

X = data[["polarity"]]
Y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0
)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_prob = clf.predict_proba(X_test)
y_pred = clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
