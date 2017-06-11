import pandas as pd

# Read the csv formatted file (DataFrame)
df = pd.read_csv("./data/train_detail.csv")

"""
    Data Munging
"""
# View the first few rows
df.head(3)
# Determines the no. of rows and columns in the dataset
df.shape
# Name of columns
df.columns
# No. of rows in the dataset
len(df)
# Get first five rows by a column name
df['Distance']
# Create categorical ranges for numerical data types
dist_ranges = pd.cut(df['Distance'], 10)
# View value counts in the distribution ranges created above
pd.value_counts(dist_ranges)

# Index on the first 6 columns of the first row ix(row, column)
df.ix[0, 0:8]
# Sort the data by specified columns and obtain a cross seciton of the data
sorted_values = df.sort_values(['Distance'])[:10]
# iloc : Index based positioning; loc: Label based positioning
sorted_values.iloc[:, 0:8].head(5)

# Obtain first 3 rows and first 3 columns
sorted_values.iloc[0:3, 0:3]
# Get set of Unique values for a column
unique_stations = df['Station Name'].unique()
unique_stations[0:100]
# Count of unique column values
len(unique_stations)
# Index into a column and get the first 10 rows
df.loc[0: 10, 'Station Name']


"""
    Data Aggregation
"""
