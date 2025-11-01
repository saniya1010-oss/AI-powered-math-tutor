from sklearn.linear_model import LogisticRegression
import numpy as np

X = []  # [difficulty, avg_time, prev_correctness]
y = []  # 1 = increase difficulty, 0 = decrease

model = LogisticRegression()

def update_model(features, target):
    X.append(features)
    y.append(target)
    if len(y) > 5:  # start training after a few rounds
        model.fit(np.array(X), np.array(y))

def predict_next(features):
    if len(y) < 5:
        return np.random.choice([0, 1])  # random at start
    return int(model.predict([features])[0])
