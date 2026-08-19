#Q10. Drop the 'English' column from original DataFrame.

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

#drop the 'English' column
df = df.drop('English', axis=1)
print("DataFrame after dropping 'English' column :", df)
print(border)


