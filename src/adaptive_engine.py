from sklearn.linear_model import LogisticRegression
from synthetic_training_dataset import get_dataset
import numpy as np
import pandas as pd

class AdaptiveEngine:
    def __init__(self):
        self.model = LogisticRegression()
        df = get_dataset()
        X = df[['accuracy', 'avg_time']]
        y = df['difficulty']
        self.model.fit(X, y)

    def predict_next_level(self, accuracy, avg_time):
        pred = self.model.predict([[accuracy, avg_time]])[0]
        return ['easy', 'medium', 'hard', 'extreme'][pred]

