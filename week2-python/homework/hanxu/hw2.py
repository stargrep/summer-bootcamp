# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:47:01 2019

@author: xuhan
"""

##Numpy

import numpy as np

#1. Create a 3x3 matrix with values ranging from 0 to 8.
a = np.arange(9).reshape(3,3)
print(a)

#2. Create a random array of size 10 and sort it
b = np.random.random(10)
b = np.sort(b)
print(b)

#3. Remove from one array those items that exist in another For example, a1 = [1, 2, 3], a2 = [1, 3] --> result = [2]
c = np.array([1,3,5,6,7])
d = np.array([2,4,5,6,7])
c = np.setdiff1d(c,d)
print(c)

#4. Get the positions where elements of two arrays match For example, a1 = [1, 2, 3, 10], a2 = [5, 4, 3, 10] --> result = [2, 3]
e = np.array([1,2,3,4,5,6,7,8,9])
f = np.array([1,1,3,3,5,5,7,7,9])
g = np.where(e == f)
print(g)

#5. Replace "Michael" with "Mike" in x x = np.array(['Hello name is Michael'], dtype=np.str)
x = np.array(['Hello name is Michael'], dtype=np.str)
y = np.char.replace(x, "Michael", "Mike")
print(y)

#6. Lex x be an array [[ 1, 2],[ 3, 4]] Rotate x 90 degrees counter-clockwise. expected result = [[3, 1], [4, 2]]
x1 = np.array([[1, 2],[3, 4]], dtype=np.str)
y1 = np.rot90(x1,3)
print(y1)

##pandas

import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'], 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3], 'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1. Create a DataFrame df from this dictionary data which has the index labels
animals = pd.DataFrame(data, index=labels)
print(animals)

#2. Return the first 3 rows of the DataFrame df.
print(animals[:3])

#3. Select just the 'animal' and 'age' columns from the DataFrame df.
print(animals.loc[:,['animal', 'age']])

#4. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
print(animals.ix[[3,4,8],['animal', 'age']])

#5. Select the rows where the animal is a cat and the age is less than 3.
print(animals.loc[(animals['animal'] == 'cat') & (animals['age'] <= 3)])

#6. Calculate the sum of all visits (the total number of visits).
sum1 = sum(animals.loc[:,'visits'])
print(sum1)

#7. In the 'animal' column, change the 'snake' entries to 'python'.
animal1 = animals.replace('snake', 'python')
print(animal1)