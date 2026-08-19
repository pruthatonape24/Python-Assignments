#Q1.Normalize the 'Math' scores using Min-Ma Scaling

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

border = "-"*60

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math': [85, 90, 78],
    'Science' : [92, 88, 80],
    'English' : [75, 85, 82]
}

df = pd.DataFrame(data)
print("DataFrame :", df)
print(border)

#Min-Max scaling
scaler = MinMaxScaler()
df['Math_Normalized'] = scaler.fit_transform(df[['Math']])
print(df)
print(border)

