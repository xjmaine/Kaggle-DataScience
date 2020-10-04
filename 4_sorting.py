import pandas as pd
# from pandas.tests.frame.test_sort_values_level_as_str import ascending
print("Setup complete.")

#read from file
reviews = pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 10) #restricts the number of rows printed

# grouping returns data index order
#sorting returns data in order specified using the sort_values()
data_review = reviews.groupby(['country', 'province']).description.agg([len])
data_reset = data_review.reset_index()

data_review = data_review.reset_index()
mi = data_review.sort_values(by='len') #outputs data in asceding order, lowest to highest on the len
# print(mi)
print(' ')

# applying descending sort
print('---Descending Sort---')
mi = data_review.sort_values(by='len', ascending=False)
# print(mi)
print(' ')

# sorting data by index using sort_index
mi = data_review.sort_index()
print(mi)
print(' ')

# sorting multiple columns using sort_values()
mi = data_review.sort_values(by=['country', 'len'])
print(mi)
print(' ')

# combining sort_values and sort_index
mi = data_review.sort_values(by=['country', 'len']).sort_index() #index overrides
print(mi)
print(' ')