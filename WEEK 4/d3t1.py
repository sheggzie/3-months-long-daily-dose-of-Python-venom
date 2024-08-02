# Load data from a CSV file into a DataFrame and perform basic operations.

import pandas as pd

file = "books.csv"

df = pd.read_csv(file) # load csv file to pandas and assing to variable df

# get basic infos
# print(df.columns)
# print(df.info())
# print(df.describe())


# select column
# columns = df['Sheggzie']
# print(columns)

# select row
# row_1 = df.iloc[0]
# rows = df.iloc[1:3] # get rows from second row to third row
# print(row_1)
# print(rows)

