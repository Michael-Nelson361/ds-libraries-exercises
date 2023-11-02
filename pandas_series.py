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

#%%

# Exercises Part 2

#%%
## 1. Capitalize all the string values in fruits.
fruits.str.capitalize()

#%%
## 2. Count the letter "a" in all the string values (use string vectorization).
sum(fruits.str.count('a'))

#%%
## 3. Output the number of vowels in each and every string value.
vowels = list('aeiou')
fruits.str.count('a|e|i|o|u')


#%%
## 4. Write the code to get the longest string value from fruits.
fruits[fruits.str.len() == max(fruits.str.len())]

#%%
## 5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]

#%%
## 6. Find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.str.count('o') >= 2]

#%%
## 7. Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]


#%%
## 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

#%%
## 9. Which string value contains the most vowels?
fruits[fruits.str.count('a|e|i|o|u') == max(fruits.str.count('a|e|i|o|u'))]

#%%

# Exercises Part 3
# Use pandas to create a Series named letters from the following string. 
# The easiest way to make this string into a Pandas series is to use list to 
# convert each individual letter into a single string on a basic Python list.

# 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

letters

#%%
# 1. Which letter occurs the most frequently in the letters Series?
# 2. Which letter occurs the Least frequently?
# 3. How many vowels are in the Series?
# 4. How many consonants are in the Series?
# 5. Create a Series that has all of the same letters but uppercased.
# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

#%%

# Use pandas to create a Series named numbers from the following list:

# `['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']`

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

#%%

# 1. What is the data type of the numbers Series?
# 2. How many elements are in the number Series?
# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
# 4. Run the code to discover the maximum value from the Series.
# 5. Run the code to discover the minimum value from the Series.
# 6. What is the range of the values in the Series?
# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

#%%

# Use pandas to create a Series named exam_scores from the following list:

# `[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]`

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#%%

# 1. How many elements are in the exam_scores Series?
# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.