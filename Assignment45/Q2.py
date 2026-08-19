#Q2.Create a gender column and perform one-hot encoding

import pandas as pd

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

#create a gender column
df['Gender'] =['Male','Male','Female']

#one-hot encoding
df = pd.get_dummies(df, columns=['Gender'], dtype = int)
print(df)
print(border)
