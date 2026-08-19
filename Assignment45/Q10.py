#Q10. Plot a boxplot for English marks to check distribution and outliers. 

import pandas as pd
import matplotlib.pyplot as plt
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
print(border)

#Count students passed
cnt = 0
for i in df['Status']:
    if i == 'Pass':
        cnt = cnt + 1
print("Total students passed :", cnt)
print(border)

#Rename 'Math' column to 'Mathematics'

df.rename(columns = {'Math':'Mathematics'}, inplace = True)
print(df)
print(border)

#plot a boxplot for english marks
plt.boxplot(df['English'], showmeans=True)

plt.title("English Marks-Distribution and outliers")
plt.ylabel("Marks")

plt.show()