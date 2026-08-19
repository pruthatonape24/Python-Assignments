#Q7.Create a bar plot of student names vs total marks.

import pandas as pd
import matplotlib.pyplot as plt

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

#display students who scored more than 85 in Science
for i in df['Science']:
    if i > 85:
        print("Students scored more than 85 in Science are:", i)
print(border)

#Replace 'Pooja' with 'puja'
df['Name'] = df['Name'].replace('Pooja', 'puja')
print("DataFrame after replacing 'Pooja' with 'puja' :", df)
print(border)

#Sort DataFrame by 'Total' in descending order
df = df.sort_values("Total", ascending = False)
print("DataFrame after sorting by 'Total' :", df)
print(border)

#Create a bar plot
plt.bar(df['Name'],df['Total'])
plt.xlabel("Student Names")
plt.ylabel("Total Marks")
plt.title("Bar Plot of Student Names vs Total Marks")
plt.show()
print(border)

