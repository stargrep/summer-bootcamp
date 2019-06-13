#!/usr/bin/env python
# coding: utf-8

# #### 2. find-first-and-last 
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 25, 35], return [5, 35]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# In[1]:


def find_first_and_last(arr):
    return [arr[0], arr[-1]]

find_first_and_last([5, 10, 15, 25, 35])


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


# #### 8. strong-password 
# Write a strong password generator function in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.

# In[22]:


def gen_psd():
    # this import is not recommended! ONLY FOR DEMO PURPOSE.
    # most of the time you may want the import at the begining of the module file.
    from random import randint
    # ascii code on the keyboard 94 keys total, no space and DEL
    symbols = list("~`!@#$%^&*()-=_+[]\{}|;':\",./<>?")
    return "" + chr(randint(65, 90)) + chr(randint(97, 122))             + chr(randint(48, 57)) + symbols[randint(0, 31)]


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




