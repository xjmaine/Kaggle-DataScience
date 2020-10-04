import pandas as pd
print("Setup complete.")

#read from file
reviews = pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 10) #restricts the number of rows printed
# print(reviews)

#creating summaries with describe()
# print(reviews.points.describe())

# creating summaries on string columns
# print(reviews.taster_name.describe())

# accessing specific summaries
# using mean (average)
print('---Mean value---')
print(reviews.points.mean())
print(' ')

# finding the list of unique values in column
print('---Unique values---')
print(reviews.taster_name.unique())
print(' ')

# finding the list of unique values occur in column
print('---Unique value occurrance---')
print(reviews.taster_name.value_counts())
print(' ')