#Q9. Create a DataFrame with missing values and fill them with column mean.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

border = "-"*60

#Create a DataFrame
data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math': [None, 90, 78],
    'Science' : [92, None, 80]
}

df = pd.DataFrame(data)
print("DataFrame with missing values : ",df)
print(border)

#fill missing valules with column mean
df['Science'] = df['Science'].fillna(np.mean(df['Science']))
df['Math'] = df['Math'].fillna(np.mean(df['Math']))

print("DataFrame after filling missing values with column mean :", df)
print(border)