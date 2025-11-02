import time
import pandas as pd

class PerformanceTracker:
    def __init__(self):
        self.data = []

    def log_attempt(self, question, correct, response_time, level):
        self.data.append({
            'question': question,
            'correct': int(correct),
            'time': response_time,
            'level': level
        })

    def summary(self):
        df = pd.DataFrame(self.data)
        if df.empty:
            return None
        accuracy = df['correct'].mean() * 100
        avg_time = df['time'].mean()
        return {
            'accuracy': round(accuracy, 2),
            'avg_time': round(avg_time, 2)
        }

    def get_dataframe(self):
        return pd.DataFrame(self.data)
