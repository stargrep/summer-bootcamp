# Q1 fibonacci
def fib(n):
  return1 and n<=2 or fib(n-1)+fib(n-2)

# Q2 find first and last
def fl(list1):
  return [list1[0], list1[-1]]
print(fl([5,4,3,2,1]))

# Q3 filter-only -even
def even(list1):
  i = 0
  list2 = []
  while(len(list1) > i):
    if(list1[i] % 2 ==0):
     list2.append(list1[i])
    i = i+1
  return list2

print(even([1,2,3,4,5]))

# Q4 leap-year
def is_leap_year(year_num):
    if year_num % 100 == 0:
        if year_num % 400 == 0:
            return True
        else:
            return False
    else:
        if year_num % 4 == 0:
            return True
        else:
            return False
print(is_leap_year(2000))

# Q5 reverse the words
def rev(x):
  y = x.split()
  return " ".join(reversed(y))
print (rev('good morning'))

# Q6 buy and sell
def max_profit(price):
    if(len(price) <= 1):
        return 0
    buy_price = price[0]
    max_profit = 0
    for i in range(1, len(price)):
        buy_price = min(buy_price, price[i])
        max_profit = max(max_profit, price[i] - buy_price)
    return max_profit
price1 = [1,2,3,4,5,4,3,2,1]
print(max_profit(price1))

# Q7 string contains
def string_contains(str1, a):
    a = str(a)
    if(str1.isdigit() and a.isdigit()):
        if(a in str1):
            return True
        else: return False
    else: return('type error')
print(string_contains('12345',5))

# Q8 strong password
import random
import string
x=string.ascii_letters  # x='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
y=string.digits   # y='0123456789'
z=string.punctuation  # z='!#$%&()*+,-./:;<=>?@[\]^_`{|}~'
def generate_pw():
    return ''.join(random.sample((x+y+z),8))
password = generate_pw()
print (password)
