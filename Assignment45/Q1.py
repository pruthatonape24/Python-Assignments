#Q1. Create Dataframe for students marks and print basic info like shape,columns, and data types.

import pandas as pd

border = "-"*60

#Create a DataFrame
data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math': [85, 90, 78],
    'Science' : [92, 88, 80],
    'English' : [75, 85, 82]
}

#print the dataframe
print(border)
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
