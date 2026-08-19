#Q3.Group students by gender and calculate average marks

import pandas as pd

border = "-"*60

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math': [85, 90, 78],
    'Science' : [92, 88, 80],
    'English' : [75, 85, 82],
    'Gender' : ['Male', 'Male', 'Female']
}

df = pd.DataFrame(data)
print("DataFrame :", df)
print(border)

#group by gender and calculate average marks

average = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

print(average)

