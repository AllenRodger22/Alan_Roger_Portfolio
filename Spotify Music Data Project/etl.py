import pandas as pd
import os
import sys

dataframes = {}
# assign directory
directory = 'scraped_raw_data_top_10'
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        dataframes[f] = pd.read_csv(f,encoding = 'latin-1')
        f = f.lstrip('scraped_raw_data_top_10')
        f = f[5:-15:]

for col in dataframes:
    dataframes[col] = dataframes[col].sort_values(by='popularity',ascending=False)

for df in dataframes:
    f = df.lstrip('scraped_raw_data_top_10')
    f = f[5::]
    dataframes[df].to_csv(f'data_staging\{f}',index = False) 