#!/usr/bin/python3

import pandas as pd

print("1) Import CSV dataset into a Pandas Dataframe…")

df = pd.read_csv("shared_cause.csv")

print("2) Show unique values in last_updated_by field.")

unique_last_updated_by = pd.unique( df.last_updated_by )

print( unique_last_updated_by )

