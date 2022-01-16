#!/usr/bin/env python
# coding: utf-8

# # Module 1

# #### In this assignment, you will work with ufo sightings data.
# - The data includes various data points about individual ufo sightings
# - Data File(s): ufo-sightings.csv

# In[1]:


###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("ufo-sightings.csv")
from nose.tools import assert_equal


# In[2]:


'''
1. Import the csv module. Load and read the UFO sightings data set, from the ufo-sightings.csv file, 
into a DictReader inside a with statement.  Assume the data file is in the same directory as the code. 

Print the field names of the data set. Iterate over the reader to put the data into a list name "ufosightings".

'''
import csv
filepath = "ufo-sightings.csv"

with open('ufo-sightings.csv','r') as csvfile:

     reader = csv.DictReader(csvfile)
    
        
     print(reader.fieldnames)
    


# your code here
import csv
filepath = "ufo-sightings.csv"

with open('ufo-sightings.csv','r') as csvfile:

    reader = csv.DictReader(csvfile)
        
    ufosightings = [] 

    for row in reader:
        ufosightings.append(row)
        
    print(ufosightings)
    
    


# In[3]:


ufosightings


# In[4]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(ufosightings, sol.ufosightings)
print("Success!")


# In[5]:


'''
2. How many sightings were there in total?  Put the count in "ufosightings_count" and print the result.
'''
# your code here

with open('ufo-sightings.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    ufosightings = []
    for row in reader:
        ufosightings.append(row)
        
    ufosightings_count = len(ufosightings)
    
    print(ufosightings_count)


# In[6]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(ufosightings_count, sol.ufosightings_count)
print("Success!")


# In[7]:


'''
3. How many sightings were there in the US?  Put the US sightings in "sightings_us" and print.

Hint: Check for ufo sightings where the country is 'us'.

'''

# your code here
with open('ufo-sightings.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
   
    ufosightings =[]
    for row in reader:
        ufosightings.append(row)

sightings_us = [row for row in ufosightings if row["country"] == "us"]
print(len(sightings_us))


# In[8]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(sightings_us,  sol.sightings_us)
print("Success!")


# In[9]:


'''
4. Let's find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each. Put the data in "fball" and print the result.

Note: Consider only the US sightings stored in "sightings_us".

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".

'''
#First, define a Python function that checks if a given duration (seconds) is "valid"

with open('ufo-sightings.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    ufosightings = []
     
    for row in reader:
        ufosightings.append(row)

ufosightings_us = [row for row in ufosightings if ["country"] == "us"]


def is_valid_duration(duration_as_string): #eliminate duration values that don't have a valid duration

# your code here

 try:
   duration = float(duration_as_string)

 except ValueError:
    return False

 else:
    return duration

fball = []

# iterate through the sightings_us

fball = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"]) > 10 and row["shape"] == "fireball"]

# output printing

for row in fball:

  print(row['datetime'], row['state'])


# In[10]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(fball, sol.fball)
print("Success!")


# In[11]:


'''
5. Sort the above list by duration. What was the datetime and duration of the longest sighting?  
Put the sorted list in "fballsorted" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Sort in reverse order.

'''
# your code here

fballsorted = sorted(fball, key = lambda x: float(x['duration (seconds)']), reverse=True)

for row in fballsorted:
        
    print((row['datetime'], row['duration (seconds)']))
    


# In[12]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(fballsorted, sol.fballsorted)
print("Success!")


# In[2]:


'''
6. What state had the longest lasting "fireball"?  Put the state in "state" and print the result.

- Check if the shape is "fireball".
- Cast the duration in seconds to a float (decimal).
- Get the record with the largest (max) duration in seconds.
- Get the state for the record.

'''
# your code here
import csv
with open('ufo-sightings.csv','r') as csvfile:
    reader =csv.DictReader(csvfile)
    
    ufosightings = [] 

    for row in reader:
        ufosightings.append(row)
        
    print(ufosightings)
        

sightings_us=[row for row in ufosightings if row["country"]=="us"]


def is_valid_duration(duration_as_string): #eliminate duration values that don't have a valid duration

# your code here

 try:
   duration = float(duration_as_string)

 except ValueError:
    return False

 else:
    return duration
# check if duration(seconds) is valid and shape is fireball
#confirmfireball = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"]) and row["shape"] == "fireball"]

confirmfireball = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"]) and row["shape"] == "fireball"]

state = max(confirmfireball, key = lambda x: float(x["duration (seconds)"]))

print(sightings_us['duration (seconds)'], sightings_us['state']) 


# In[16]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(state, sol.state)
print("Success!")


# In[21]:


'''
7. Let's assume that any sighting (of any shape) of 0 seconds is insignificant. 
Write code to filter out these extraneous records and get the shortest sighting overall now.  
Put the minimum duration in "min_duration" and print the result.  
Use ufosightings
Note: Consider all sightings stored in "ufosightings".

'''
# your code here
import csv
import pandas as pd
filepath = "ufo-sightings.csv"

with open('ufo-sightings.csv','r') as csvfile:

    reader = csv.DictReader(csvfile)


    ufosightings = []

    for row in reader:
        ufosightings.append(row)
    print(ufosightings)


def is_valid_duration(duration_as_string): #eliminate duration values that don't have a valid duration

# your code here

   try:
    if float(duration_as_string) > 0.0:
        return True
    else: 
        return False
   except ValueError:
    return False
duration_valid = [row for row in ufosightings if (is_valid_duration(row["duration (seconds)"]))]
min_duration = min(duration_valid, key = lambda x: x["duration (seconds)"])
print(min_duration)


# In[22]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(min_duration, sol.min_duration)
print("Success!")


# In[ ]:


'''
8. What are the top 3 shapes sighted, and how many sightings were there for each? 

Note: Consider all sightings stored in "ufosightings".

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''
#Create a new list containing values from the "shape" column in ufosightings.
# your code here


import csv
import pandas as pd
filepath = "ufo-sightings.csv"

with open('ufo-sightings.csv','r') as csvfile:

    reader = csv.DictReader(csvfile)


    ufosightings = []

    for row in reader:
        ufosightings.append(row)
    print(ufosightings)
    
    
sightings_shapes = [row["shape"] for row in ufosightings]

sightings_shapes

#Create a new dictionary with values of that column as keys and the counts as values.
# your code here

count = {}

for i in range(len(sightings_shapes)):
    count[sightings_shapes[i]] = sightings_shapes.count(
    sightings_shapes[i])
        
print(count) 
    
    
#Get a list of the dictionary keys and values (use the items() method) and sort them in reverse order, from greatest (most sightings) to least.
#Get and print the top 3.
# your code here

x = count.items()


shapes = sorted(x, key=lambda x: x[sightings_shapes], reverse=True)
top3shapes = shapes[0:3]
top3shapes


# In[ ]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(sightings_shapes, sol.sightings_shapes)
print("Success!")


# In[ ]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(count, sol.count)
print("Success!")


# In[ ]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(top3shapes, sol.top3shapes)
print("Success!")

