from sklearn.tree import DesicionTreeClassifier
from synthetic_training_dataset import get_dataset

class AdaptiveEngine:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        df = get_dataset()
        X = df[['Accuracy', 'Time taken']]
        y = df['difficulty']
        self.model.fit(X,y)

def predict_difficulty(self, accuracy, time_taken):
    features = [[accuracy, time_taken]]
    prediction = self.model.predict(features)
    return prediction[0]

