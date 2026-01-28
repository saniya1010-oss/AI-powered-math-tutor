import numpy as np
import pandas as pd
#specify number of players

num_players = 50000
accuracy = np.clip(
    np.random.normal(50, 25, num_players),
    0, None
) #gaussian distribution with mean 50, and std 25
avg_time = np.clip(
    np.random.normal(30, 15, num_players),
    0, None)

#specify difficulty levels
diff = np.where(
    (accuracy >= 75) & (avg_time < 15), 'extreme',
    np.where(
        (accuracy >=70) & (avg_time < 25), 'hard',
        np.where(
            (accuracy >= 60) & (avg_time < 35), 'medium',
            np.where(
                (accuracy >= 45) & (avg_time < 40), 'normal',
                'easy'
            )
        )
    )
)

df = pd.DataFrame({
    'Accuracy' : accuracy,
    'Time Taken' : avg_time,
    'Difficulty Level' : diff
})

def get_dataset():
    return df

data = get_dataset()
print(f'Number of difficulty levels {data['Difficulty Level'].value_counts()}')
