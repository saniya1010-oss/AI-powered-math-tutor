import numpy as np
import pandas as pd

# number of players
n = 1000 #adjustable
accuracy = np.random.normal(70, 15, n).clip(0, 100)
avg_time = np.random.normal(8, 3, n).clip(1, 20)

# ---Hierarchy of Difficulty Levels---
difficulty = np.where(
    (accuracy > 90) & (avg_time < 5), 3, #extreme
    np.where(
        (accuracy > 85) & (avg_time < 10), 2,  # hard
            np.where((accuracy > 60) & (avg_time < 20), 1,  # medium
                    0 #easy
            )
        )
    )

df = pd.DataFrame({
    'accuracy': accuracy,
    'avg_time': avg_time,
    'difficulty': difficulty
})

def get_dataset():
    return df
