""" -- !!! IMPORTANT !!! --

  1. Use Docstrings in functions
  2. DRY 
  3. Functions should 'Do One Thing'
  4. Do not use mutable default arguments.
  5. The ideal is to strive to make your code so readable, to use such good variable names 
     and function names, and to structure it so well that you no longer need any comments 
     to explain what the code is doing. Just a few here and there to explain why.

"""

#  ---- Read multiple files and concat into single df
import pandas as pd
import glob
import os

path = "/home/project/my_folder"
all_files = glob.glob(os.path.join(path, "*Timesheet*.csv"))


datasets = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None)
    datasets.append(df)

data = pd.concat(datasets, ignore_index=True)

# -----------------------------------------------------------------------------

# ---- find duplicates in a list
import collections

a = [1, 1, 2, 34, 5, 34]
[item for item, count in collections.Counter(a).items() if count > 1]

# -----------------------------------------------------------------------------

# ---- Start a Timer
import time

Total_start_time = time.time()
print(" Total run-time: ", "%s seconds" % round((time.time() - Total_start_time), 2))

# -----------------------------------------------------------------------------
