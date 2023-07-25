#!/usr/bin/python3

import pandas as pd

print("1) Import CSV dataset into a Pandas Dataframe")
df = pd.read_csv("shared_cause.csv")

print("\n2) General information about the Dataframe")
print('DataFrame shape:', df.shape)
print('DataFrame size:', df.size)
print(df.info())

print("\n3) Show the first five rows of the dataframe")
print(df.head())

print("\n4) Display rows 100 through 130 and columns 1-3 ONLY\n")
print(df.iloc[ 100:131, 0:3])
print()
