import os
import pandas as pd
from sklearn.preprocessing import StandardScaler import numpy as np

os.getcwd() #get current working directory
os.chdir("/Users/shenzhou/Desktop/) #change the current working directory to specified new path
os.listdir() #list all files in the current working directory

df=pd.read_csv("tumor_cells.csv",header=None) # tumor_cells.csv is an example file

pd.set_option('display.max_columns', 10) # show 10 columns
pd.set_option('display.max_columns', None) # show all columns
pd.set_option('display.max_rows', 10) # show 10 rows
pd.set_option('display.max_rows', None) # show all rows
