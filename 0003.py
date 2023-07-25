#!/usr/bin/python3

import pandas as pd

print("1) Import CSV dataset into a Pandas Dataframe")
df = pd.read_csv("shared_cause.csv")

# make sure all values in 'cause_description'
df2 = df[~df.cause_name.isnull()]

# could further filter
df2 = df2[df2["cause_name"].str.contains("disease")]

print(df2.iloc[ 1:51, 0:5])


