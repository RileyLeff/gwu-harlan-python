# pandas has a nice dataframe type that we will use
import numpy as np
import pandas as pd
import datetime

path_to_data = 'data/cats.csv'

catdf = pd.read_csv(path_to_data)

catdf['timestamp'] = pd.to_datetime(catdf['timestamp'])

# run "catdf" in the interpreter to inspect the dataset!



# CHALLENGE QUESTIONS:
#   which cat appears most frequently?
#   which cat/activity/location combo appears most frequently? 
#   what's the longest streak of one cat consecutively?
#   what's the longest streak of alternating cats?
#   do all unique combos of cat x location x action occur?
#   which unique combo takes the longest to occur?


# HINT:
#   to get the dataframe sorted by date:
    #   catdf = catdf.sort_values(by = 'timestamp')

#   to select a column:
    #   catdf['column_name']

#   to get rows from a column:
    #   catdf['column_name'][row_index]

#   think about loops
#   think about conditional statements