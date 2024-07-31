import os
import pandas as pd
from sklearn.preprocessing import StandardScaler import numpy as np

os.getcwd() #get current working directory
os.chdir("/Users/shenzhou/Desktop/) #change the current working directory to specified new path
os.listdir() #list all files in the current working directory

pd.set_option('display.max_columns', 10) # show 10 columns
pd.set_option('display.max_columns', None) # show all columns
pd.set_option('display.max_rows', 10) # show 10 rows
pd.set_option('display.max_rows', None) # show all rows
df=pd.read_csv("tumor_cells.csv",header=None) # tumor_cells.csv is an example file

df.head(5)#read the first 5 rows
df.tail(5)# read the last 5 rows
df.describe()#show descriptive statistics of each column
df.isnull().sum() #check counts of missing values in each column
df[3].fillna(df[3].mean(),inplace=True) # replace the missing value with that column mean

df[1].replace(to_replace=["B","M"],value=[0,1],inplace=True) # replace "B" with 0 and "M" with 1


# create a data frame by specifying values for each column in a dictionary format
df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
     index = [1, 2, 3]) # if not specifying the index, the default index would start with 0
# create a data frame by specifying values for each row in a list format
df = pd.DataFrame(
    [[4, 7, 10],
     [5, 8, 11],
     [6, 9, 12]],
     index = [1, 2, 3],
     columns = ["a", "b", "c"])
# create a wide data frame
df_wide = pd.DataFrame(
  {"student": ["Andy", "Bernie", "Cindy", "Deb"],
   "english": [10, 100, 1000, 10000],  # english grades
   "math":    [20, 200, 2000, 20000],  # math grades
   "physics": [30, 300, 3000, 30000]   # physics grades
  })
# use melt to transfer wide data to long data 
df_long = df_wide.melt(
    id_vars = "student",
    var_name = "class",  # new variable name (for different categories)
    value_name = "grade" # new variable name (for different values)
  )
# Use pivot to transfer long data to wide data
df_long.pivot(
    index = "student",
    columns = "class",
    values = "grade"
  )


pd.concat([df1, df2])# append the two data frames vertically, along the rows
pd.concat([df1, df2], axis = 1)# append the two data frames horizontally, along the columns

df.sort_values("A") # # sort values of column A in a data frame in ascending order
df.sort_values("A", ascending = False) # decending order

df_copy = df.copy() # make a copy of the original data frame
df.rename(columns = {"a": "A", "b": "B"})# rename column a to A and b to B 
df.drop(columns = ["A", "B"])# drop columns A and B from a data frame

df[df["a"] >= 5] # extract rows that meet a logical criterion
df.where(df["a"] >= 5, -999) # replace rows not meeting a logical criterion with -999

df_missing = pd.DataFrame(
  {"a": [1, 2, 3],
   "b": [4, np.NaN, 6],
   "c": [7, 8, 9]})# create a data frame with missing values
df_missing.dropna(subset = ["b"])# drop the row with the missing value in column "b"

median = df_missing["b"].median()
df_missing["b"].fillna(median, inplace = True)# fill missing values by the median of a column

df.sample(frac = 0.5)# randomly select fraction of rows
df.sample(n = 1)# randomly select n rows

df.loc[:, "a":"c"]# select all columns between "a" and "c", including "c" (loc: label-based position vs. iloc: integer-based position)
df.iloc[:, [1, 2]]# select all columns in positions 1 and 2 (first position is 0)
df.iloc[[1, 2]]# select the second and third rows
df.loc[df["a"] >= 5, ["a", "c"]]# select rows meeting logical condition, and only specific columns

df.sum(axis = 0) # sum values of each column (along the rows) in a data frame,axis = 0 is the default, which can be omitted
df.sum(axis = 1)# sum values of each row (along the columns) in a data frame
df.count()# count non-na/null values of each column
df.quantile([0.25, 0.5, 0.75])# quantiles of each column

