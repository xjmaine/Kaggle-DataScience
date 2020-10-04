import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
# from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples':[30], 'Bananas':[21]})

# Check your answer
# q1.check()
print(fruits)
print('___________________________________')

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

print(fruit_sales)
print('___________________________________')

# Create a variable ingredients with a Series that looks like:

# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)