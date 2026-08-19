#Q8. Plot a histogram of math marks.

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

#Export the final DataFrame to a CSV file
Filename = open("DataFrame.csv", "w")

Filename.write(str(df))

print("DataFrame exported to CSV file successfully.")
Filename.close()

print(border)

#plot a histogram
plt.hist(df['Math'])

plt.title("Math marks")
plt.xlabel("Marks")
plt.ylabel("Number of students")

plt.show()

