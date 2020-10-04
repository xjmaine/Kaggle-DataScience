# Lesson - 1 Creating data
# using dataframes and series

import pandas as pd
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2], 'Maybe': [57, 25]}, index=['Month1', 'Month2'])

print(df)

print('---------Data frame list 2-------')

df2=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue':['Pretty good', 'Bland.']}, index = ['Sample A', 'Sample B'])
print(df2)
print('')

# series is just a list
ser= pd.Series([1,2,3,4,5,6])
print(ser)

ser2= pd.Series([75,15, 96], index=['Sales Month 1',
 'Sales Month 2', 
 'Sales Month 3'], name='Product A' )
print(ser2)