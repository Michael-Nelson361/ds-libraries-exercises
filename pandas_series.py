#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:44:14 2023

@author: manelson
"""

# Exercises Part 1

### Initialize the conditions for part 1
import pandas as pd
import numpy as np

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#%%
## 1. Determine the number of elements in fruits.
### A: 17
len(fruits)

#%%
## 2. Output only the index from fruits.
fruits.index

#%%
## 3. Output only the values from fruits.
fruits.values

#%%
## 4. Confirm the data type of the values in fruits.
fruits.dtype

#%%
## 5. Output only the first five values from fruits. 
    # Output the last three values. Output two random values from fruits.
fruits.head()
fruits.tail(3)
fruits.sample(2)

#%%
## 6. Run the .describe() on fruits to see what information it returns when 
    #called on a Series with string values.
fruits.describe()

#%%
## 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

#%%
## 8. Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

#%%
## 9. Determine the string value that occurs most frequently in fruits.
fruits.value_counts().head(1)

#%%
## 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts().tail(1)

