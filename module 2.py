#!/usr/bin/env python
# coding: utf-8

# ## Module 2
# 
# #### In this assignment, you will work on movie data from IMDB.
# - The data includes movies and ratings from the IMDB website
# - Data File(s): imdb.xlsx
# 
# #### Data file contains 3 sheets:
# - “imdb”: contains records of movies and ratings scraped from IMDB website
# - “countries”: contains the country (of origin) names
# - “directors”: contains the director names

# In[1]:


###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("imdb.xlsx")
from nose.tools import assert_equal
from pandas.util.testing import assert_frame_equal, assert_series_equal


# In[2]:


""" Q1: 
Load and read the 'imdb.xlsx' file. Read the 'imdb' sheet into a DataFrame, df.
"""

import pandas as pd

# your code here
xls = pd.ExcelFile('imdb.xlsx')

df = xls.parse('imdb')


# In[28]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(df, sol.df)


# In[10]:


""" Q2: 
Store the dimensions of the DataFrame as a tuple in a variable called 'shape' and print it.

Hint: A tuple is made up of comma separated values inside parenthesis.  e.g. (1, 2)
"""

# your code here
shape = tuple(df)
print(shape)


# In[11]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(shape, sol.shape)


# In[13]:


""" Q3: 
Store the column titles and the types of data in variables named 'columns' and 'dtypes', then print them.
"""
# your code here
columns = df.columns
dtypes = df.dtypes

print(columns, dtypes)


# In[14]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(columns.all(), sol.columns.all())
assert_series_equal(dtypes, sol.dtypes)


# In[15]:


""" Q4: 
Examine the first 10 rows of data; store them in a variable called first10
"""

first10= df.head(10)
first10
# your code here


# In[16]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(first10, sol.first10)


# In[17]:


""" Q5: 
Examine the first 5 rows of data; store them in a variable called first5
"""

first5 = df.head()
first5
# your code here


# In[18]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(first5, sol.first5)


# In[19]:


""" Q6: 
Import the "directors" and "countries" sheets into their own DataFrames, df_directors and df_countries.
"""

df_directors = pd.read_excel('imdb.xlsx', sheet_name = 'directors')

df_countries = pd.read_excel('imdb.xlsx', sheet_name = 'countries')


# your code here


# In[20]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(df_directors, sol.df_directors)
assert_frame_equal(df_countries, sol.df_countries)


# In[22]:


""" Q7: 
Check the "directors" sheet
1. Count how many records there are based on the "id" column. (To get the number of records per "id", 
   use the value_counts method.) Store the result in a variable named count.
2. Remove the duplicates from the directors dataframe and store the result in a variable called df_directors_clean.
"""

# your code here
#1
count = df_directors['id'].value_counts()
count 

#2
df_directors_clean = df_directors.drop_duplicates()


# In[23]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(count, sol.count)
assert_frame_equal(df_directors_clean, sol.df_directors_clean)


# In[ ]:





# In[ ]:




