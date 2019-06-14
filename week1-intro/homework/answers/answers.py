#!/usr/bin/env python
# coding: utf-8

# #### 1. fibonacci 
# Get the n-th fibonacci number

# In[26]:


def fibonacci(n): 
    if n<0: 
        print("Invalid value") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 
  

fibonacci(5)


# #### 2. find-first-and-last 
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 25, 35], return [5, 35]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# In[1]:


def find_first_and_last(arr):
    return [arr[0], arr[-1]]

find_first_and_last([5, 10, 15, 25, 35])


# #### 3. filter-only-even 
# Given a list saved in a variable: a = [1, 4, 9, 64, 81, 100] and return [4, 64, 100] Write program that takes this list a and makes a new list that has only the even elements of this list in it.

# In[41]:


import functools 

# solution 1
a = [1, 4, 9, 64, 81, 100] 
b = list(filter(lambda x: x % 2 == 0, a))
print("solution 1: ", b)

# solution 2
def even_filter(a):
    b = []
    for num in a:
        if num % 2 == 0:
            b.append(num)
    return b

b = even_filter(a)
print("solution 2: ", b)


# #### 4. leap-year 
# Given a year and return if it's a leap-year. input: 2000 and output: True.

# In[2]:


def is_leap_year(year):
    if year < 0: 
        return False
    return (year % 400 == 0) or             ((year % 4 == 0) and (year % 100 != 0))

print(is_leap_year(-1) == False)
print(is_leap_year(0) == True)
print(is_leap_year(1996) == True)
print(is_leap_year(2000) == True)
print(is_leap_year(2100) == False)


# #### 5. Reverse string
# Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# 
# My name is Mike
# 
# Then I would see the string:
# 
# Mike is name My
# 
# shown back to me.

# In[57]:


a = 'My name is Mike'

# solution 1
temp = a.split()
temp.reverse()
b = ' '.join(temp)
print("solution 1: ", b)

# solution 2
b = ' '.join(a.split()[::-1])
print("solution 2: ", b)


# #### 6. buy-and-sell 
# Say you have an array for which the i-th element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one.
# 
# 
# Example 1:
# 
# 
# Input: [7,1,6,4,5,3] Output: 5 Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 6), profit = 6-1 = 5.
# 
# 
# Input: [7,4,3,2] Output: 0 Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 

# In[3]:


def buy_and_sell(prices):
    if len(prices) < 2: #at least two days for trading
        return 0
    
    profit = 0
    buy_price = prices[0]
    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            current_profit = price - buy_price
            if current_profit > profit:
                profit = current_profit
    return profit
                
print(buy_and_sell([7, 1, 6, 4, 5, 3]) == 5)
print(buy_and_sell([7, 4, 3, 2]) == 0)


# #### 7. sting-contains 
# Write a function that takes sorted string with only numbers and find if a number (from 0 to 9) is in it. Example: string_contains("13589", 7) -> False string_contains("00233", 0) -> True

# In[80]:


def string_contains_1(s, target):
    for c in s:
        if c == str(target):
            return True
    return False

def string_contains_2(s, target):
    for c in s:
        if int(c) == target:
            return True
    return False

import re
def string_contains_3(s, target):
    return re.search("[%d]" % target, s) != None

print(string_contains_1("13589", 7))
print(string_contains_1("00233", 0))

print(string_contains_2("13589", 7))
print(string_contains_2("00233", 0))

print(string_contains_3("13589", 7))
print(string_contains_3("00233", 0))


# #### 8. strong-password 
# Write a strong password generator function in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.

# In[22]:


def gen_psd():
    # use string and random pkg
    import random
    import string
    return "".join(
            random.sample(string.ascii_lowercase, 1) + \
            random.sample(string.ascii_uppercase, 1) + \
            random.sample(string.digits, 1) + \
            random.sample(string.punctuation, 1) \
        )


# check_psd is to check if a password string is strong.
def is_strong_psd(psd):
    uppers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowers = list("abcdefghijklmnopqrstuvwxyz")
    numbers = list("0123456789")
    return len(list(filter(lambda x : (x in uppers) or (x in lowers) or (x in numbers), list(psd))))             < len(psd)


print(is_strong_psd("qQ1@") == True)
print(is_strong_psd("qQ1") == False)
print(is_strong_psd(gen_psd()) == True)
print(gen_psd())  # print a random psd


# In[ ]:




