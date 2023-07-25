#!/usr/bin/python3

import pandas as pd

print("1) Import CSV dataset into a Pandas Dataframe")
df = pd.read_csv("shared_cause.csv")

# remove nulls
# df2= df[df.notnull().all(1)]

# make sure all values in 'cause_description'
df2 = df[~df.cause_description.isnull()]
# df2 = df2[~df2.cause_id_2010_gbd_round.isnull()]
print(df2.iloc[ 1:51, 0:7])


