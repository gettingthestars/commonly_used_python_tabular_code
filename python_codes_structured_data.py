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
df.describe()#show descriptive statistics of each column
df.isnull().sum() #check counts of missing values in each column
df[3].fillna(df[3].mean(),inplace=True) # replace the missing value with that column mean

df[1].replace(to_replace=["B","M"],value=[0,1],inplace=True) # replace "B" with 0 and "M" with 1

pd.concat([df1, df2])# append the two data frames vertically, along the rows
pd.concat([df1, df2], axis = 1)# append the two data frames horizontally, along the columns

df.sort_values("A") # # sort values of column A in a data frame in ascending order
df.sort_values("A", ascending = False) # decending order

df_copy = df.copy() # make a copy of the original data frame
df.rename(columns = {"a": "A", "b": "B"})# rename column a to A and b to B 
df.drop(columns = ["A", "B"])# drop columns A and B from a data frame
