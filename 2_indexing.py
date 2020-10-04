import pandas as pd
import csv
import os
print("Setup complete.")

#read from file
reviews = pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
# print(reviews.head())

# accessing title property
# print(reviews.country) #style one
print('________________')

# using the indexing operator []
# print(reviews['country'][0]) 
print('________________')

# using pandas integer based indexing selection
#row based retrival
# print(reviews.iloc[0])
print('________________')
print(' ')

#using column based retrival
#print(reviews.iloc[:, 0])

#select range
# print('-----Range iloc-----')
# print(reviews.iloc[:3,0])

# using the loc[:, ''] specific columns can be specified
# print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

# Conditional slection using loc
# print('---conditional selection with loc---')
# print(' ')
# print(reviews.loc[reviews.country =='Italy'])
# print(' ')

# print('---conditional selection: using &---')
# print(' ')
# print(reviews.loc[(reviews.country =='Italy') & (reviews.points >=90)] )
# print(' ')

# print('---conditional selection: using or |---')
# print(' ')
# print(reviews.loc[(reviews.country =='Italy') | (reviews.points >=90)] )
# print(' ')

# pandas built in function 'isin'
print('---In-built panda function: isin---')
print(' ')
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
print(' ')

#filter out values
print('---In-built panda function: notnull()---')
print(' ')
print(reviews.loc[reviews.price.notnull()])
print(' ')