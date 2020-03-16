# -*- coding: utf-8 -*-
"""

File contains code for generic, standard data science projects. 
Process is dedicated for data in pandas DataFrame format.

"""

#=============================================================================#
# Data cleaning #
#===============#

import pandas as pd

#==========================#
# Check for variable types #
#==========================#

# Show number of observations in particulars columns, null, type of column
df.info() 

"""

string detection - if the column is object type, but supposed to be 
                float or integer, and couldn't be converted to float 
                or integer, there may be some string values

nan detection - there is number of observations pointed out, if number is 
                lower than number of rows there may be "nan" value in the 
                column (null detection may not work, column may be "non-null", 
                but have a nan)

"""

#===============================#
# Check NULL values in a column #
#===============================#

dict_01 = {'one': ['A', 'B', 'C', 'D'], 
              'two': [1, 2 , np.nan, 4], 
              'three': ['a', 'b', 'c', 'd']}
dataframe_01 = pd.DataFrame(dict_01)


# Check how many NULL values is in df
pd.isnull(dataframe_01['two']).sum()


#====================================#
# Check for min and max values, etc. #
#====================================#
# Check if values are as expected, if there are certain assumptions

dataframe_01.describe(include='all')

""" 

Check for:
    
count, unique, top, freq, mean, std, min, quartiles, 25%, 50%, 75%, max

"""
