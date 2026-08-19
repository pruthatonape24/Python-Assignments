#Q5.Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.

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

#Calculate Total
df['Total'] = df[['Math','Science','English']].sum(axis=1)

#Add status 
df['Status'] = df['Total'].apply(
    lambda x : 'Pass' if x >= 250 else 'Fail'
)

print(df)
