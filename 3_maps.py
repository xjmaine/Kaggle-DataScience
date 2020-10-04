import pandas as pd
print("Setup complete.")

#read from file
reviews = pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5) #restricts the number of rows printed

# Maps has two functions
# map() and apply()

# using map() - takes a series value and returns a series value
review_points_mean = reviews.points.mean()
print_this = reviews.points.map(lambda p: p - review_points_mean)
print(print_this)
print(' ')


# apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
# print('using apply method')

# def remean_points(row):
#     row.points -= review_points_mean
#     return row
# print(reviews.apply(remean_points, axis='columns'))

# using pandas built-in functions for maps
print('----map in-built----')
review_points_mean = reviews.points.mean()
gath = reviews.points - review_points_mean
print(gath)

print(' ')
print('combine columns')
combined_columns = reviews.country+"-"+ reviews.region_1
print(combined_columns)