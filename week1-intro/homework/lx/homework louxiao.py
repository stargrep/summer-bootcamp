import random

def fibonacci(index):
    """
    fibonacci implementation in python, use iteration.
    (0), 1, 1, 2, 3, 5, 8, 13, 21, 34
    index 0 -> 0
    index 1 -> 1
    index 2 -> 1
    ...
    index 7 -> 13
    ...
    :param index: the i-th fibonacci number
    :return:
    """
    # when index < or == 0, value is 0
    if index < 1:
        return 0
    # when index == 1 or == 2, value is 1
    if index < 3:
        return 1
    # fibonacci function is current index = previous + the one before previous
    return fibonacci(index - 1) + fibonacci(index - 2)


print(fibonacci(9))  # should be 34

'''
Q2. find-first-and-last
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 25, 35], return [5, 35]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''


# function starts here
def ret_list(lis):
    # get the first and last number
    a = lis[0]
    b = lis[-1]
    return [a, b]


# test it
print(ret_list([1, 2, 3]))


'''
Q3. filter-only-even
Given a list saved in a variable: a = [1, 4, 9, 64, 81, 100] and return [4, 64, 100] 
Write program that takes this list a and makes a new list that has only the even elements of this list in it. 

Bonus: Use only one line.
'''
import math


# function starts here
def issqrt(a):
    return int(math.sqrt(a)) == math.sqrt(a)  # decide whether it is a even number


def even(a):
    for i in a:
        if not issqrt(i):
            a.remove(i)  # drop those numbers which are not even according to function issqrt
    return a


# test it
print(even([1, 4, 5, 243, 6]))  # turn out to be true



'''
Q4. leap-year
Given a year and return if it's a leap-year.
input: 2000 and output: True.
'''


def isleap(a):
    if a % 4 == 0:   # if it is a leap year, then after modding it , the result should be zero
        print("True")  # print the judgemental result


# test it
isleap(2000)
isleap(2001)


'''
Q5. Write a program that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

My name is Mike

Then I would see the string:
      
Mike is name My

shown back to me.
'''


def in_ver(str):
    lis = str.split() # split the sentence into words
    lis.reverse() # reverse the order of words in a list
    return lis


def rejoi(str):
    # join the three words with ' ' in between
    gap = ' '
    # whole sentence is ws
    ws = gap.join(in_ver(str))
    return ws


# test 1
print(in_ver("My name is Mike"))
# this test has passed

# test 2
print(rejoi('My name is Mike'))
# this test has passed


'''
Q6. buy-and-sell
Say you have an array for which the i-th element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
    design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,6,4,5,3]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 6), profit = 6-1 = 5.

Input: [7,4,3,2]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


# figure out the optimal outcome on each day
def opt_day(lis):
    outcome = []
    for i in range(len(lis)-1):  # the minus one is really important
        can_buy = lis[i+1:]  # find the days you can sell
        can_buy.sort(reverse=True)  # find the optimal price to sell
        outcome.append(can_buy[0])  # add the price to the list
    return outcome


# figure out the best outcome
def max_p(lis):
    outcome = opt_day(lis)
    profit = []
    for i in range(len(outcome)):
        if outcome[i] >= lis[i]:  # if there is profit, register it in profit
            profit.append(outcome[i]-lis[i])
        else:   # if not, accept zero return
            profit.append(0)
    profit.sort()
    return profit[-1]


# test it
print(opt_day([7, 1, 6, 4, 5, 3]))
# pass
print(max_p([7, 1, 6, 4, 5, 3]))
# pass



'''
Q7. sting-contains
Write a function that takes sorted string with only numbers and find if a number (from 0 to 9) is in it. 
Example: 
string_contains("13589", 7) -> False
string_contains("00233", 0) -> True
'''


def string_contains(st_r, num):
    '''all = int(st_r)
    res = all
    jud = False
    while res > 0:
        digit = res % 10
        if digit == num:
            jud = True
            break
        res = (res - digit) / 10

    return jud'''
    # above is failed due to less scrupulous concern over 0
    judge = False
    for i in range(len(st_r)):
        if int(st_r[i:i+1]) == num:
            judge = True
    return judge


# test it
print(string_contains("13589", 7))
# pass
print(string_contains("00233", 0))
# pass


'''
Q8. strong-password
Write a strong password generator function in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
'''


def strong_pass(t):  # i is the digits of your key
    cnt_lc = 0  # define the occurance of each type
    cnt_uc = 0
    cnt_n = 0
    cnt_sb = 0
    key_lis = []  # include the elements
    while cnt_lc == 0 or cnt_uc == 0 or cnt_n == 0 or cnt_sb == 0 :  # ensure that all of the four kind exist.
        key_lis = []
        for i in range(t):
            posit = random.randint(48, 126)  # generate random asc number
            if posit in range(48, 58):  # record type
                cnt_n += 1
            elif posit in range(65, 91):
                cnt_uc += 1
            elif posit in range(97, 123):
                cnt_lc += 1
            else:
                cnt_sb += 1
            key_lis.append(chr(posit))  # add to they element set

    gap = ''
    str_key = gap.join(key_lis)  # combine the elements into a string
    return str_key


# test it
print(strong_pass(8))
print(strong_pass(8))
print(strong_pass(8))
# pass




