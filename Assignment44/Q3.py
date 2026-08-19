#Q3. Add a new column 'Total' to DataFrame as the sum of all subject marks.

import pandas as pd

border = "-"*60

#Create a DataFrame
data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math': [85, 90, 78],
    'Science' : [92, 88, 80],
    'English' : [75, 85, 82]
}

df = pd.DataFrame(data)
print("DataFrame : \n", df)
print(border)

#print the shape, columns, and data types
print("Shape of DataFrame : ", df.shape)
print(border)
print("Columns of DataFrame : ", df.columns)
print(border)
print("Datatypes of DataFrame :", df.dtypes)
print(border)

#print the descriptive statistics
print("Descriptive Statistics of DataFrame : \n", df.describe())
print(border)

#Add a new column 'Total'
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
print("DataFrame after adding 'Total' column : \n", df)
print(border)

