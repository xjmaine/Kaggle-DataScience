import pandas as pd
import re
from pip._vendor.progress import counter
print("Setup complete.")

#read from file
reviews = pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5) #restricts the number of rows printed

# What is the median of the points column in the  reviews DataFrame?
median_points = reviews.points.median()
# print(median_points)

# What countries are represented in the dataset? (Your answer should not include any duplicates.)4
countries = reviews.country.unique()
# print(countries)

# How often does each country appear in the dataset? Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
reviews_per_country = reviews.country.value_counts()
# print(reviews_per_country)

# Create variable centered_price containing a version of the price column with the mean price subtracted.
mean_price = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - mean_price)
# print(centered_price)

# I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset
ratio_value = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.title.loc[ratio_value]
# print(bargain_wine)

# There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or "fruity"? Create a Series  descriptor_counts counting how many times each of these two words appears in the description column in the dataset.
# series_count = pd.Series(reviews.description)
# descriptor_counts = series_count.str.count(['tropical'|'fruity'])
# print(descriptor_counts)

#use advanced for loop (wordlist)
def search_word(column, key):
    counter=0
    for description in column:
        words = description.split()
        for word in words:
            if word.lower() == key:
                counter +=1
    return counter

search_word1=reviews.description.map(lambda find: 'tropical' in find).sum()
search_word2 = reviews.description.map(lambda find: 'fruity' in find).sum()
descriptor_counts = pd.Series([search_word1, search_word2], index=['tropical', 'fruity'])
# print(descriptor_counts)


# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.

# Create a series star_ratings with the number of stars corresponding to each review in the dataset
def convert_stars(row):
    stars = 0
    if 'Canada' == row.country:
        stars=3
    elif row.points >= 95:
        stars=3
    elif row.points >= 85:
        stars=2
    else:
        stars=1
    return stars
star_ratings = reviews.apply(convert_stars, axis='columns')
print(star_ratings)



# If it benefits you, build a higher table, not a higher fence