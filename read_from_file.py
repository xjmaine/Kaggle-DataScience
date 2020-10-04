import pandas as pd

# working with csv files using read_csv()

survey_review= pd.read_csv("C:/Users/Rosie/Desktop/snips/AI/Pandas/bo-19-1.csv", index_col=0)
print(survey_review.shape)
# survey_review.shape
# survey_review.head()