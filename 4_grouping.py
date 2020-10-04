import pandas as pd
from astropy.modeling.tests import data
print("Setup complete.")

#read from file
reviews = pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 10) #restricts the number of rows printed

# print(reviews.head())

pointz = reviews.points.count()
# print('Points 1: ',pointz)
# print(' ')

pointz = reviews.groupby('points').points.count()
# print('Points 2: ',pointz)
# print(' ')

# value_counts() is short form of groupby()
pointz = reviews.points.value_counts()
# print('Points 3: ',pointz)
print(' ')

# example using a summary function
points_min = reviews.groupby('points').price.min()
# print(points_min)


# data can be manipulate as desired using the apply() map function
data = reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
# print(data)
print(' ')

# groupings can be done on multiple columns fir finer control
data = reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
# print(data)
print(' ')


# groupby() has another function agg() which generates statistical summaries
data = reviews.groupby(['country']).price.agg([len, min, max, sum, 'mean'])
# print(data)
print(' ')

# Multi-indexes using groupby()
# multi-index has multiple levels
data_review = reviews.groupby(['country', 'province']).description.agg([len])
print(data_review)
print(' ')
# type used
mi = data_review.index
print(type(mi)) #outputs: <class 'pandas.core.indexes.multi.MultiIndex'>
print(' ')

# data can be reversed back to regular index using
# reset_index()
data_reset = data_review.reset_index()
print(data_reset)