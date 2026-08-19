#Q4.Plot a pie chart of subject marks for 'Sagar'.

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

#select sagar

sagar = df[df['Name'] == 'Sagar'].iloc[0]

subjects = ['Math', 'Science', 'English']
marks = [sagar['Math'], sagar['Science'], sagar['English']]

plt.pie(
    marks,
    labels = subjects,
    autopct = "%1.1f%%",
)

plt.title("Subject marks for sagar")
plt.show()
