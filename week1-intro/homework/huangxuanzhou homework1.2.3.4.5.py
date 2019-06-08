#!/usr/bin/env python
# coding: utf-8

# In[9]:


number=20  # which number in fibonacci list do you want?(take the 20th as an example)
fibo=[1,1] #set up a basic list
for i in range(2,1000): #set up a cycle
    a=fibo[i-1]+fibo[i-2] #get the fibonacci list
    fibo.append(a) #add the new number into the list
print(fibo[number]) #return the asked number


# In[13]:


def blabla(list): #define a function
    number=len(list) #how many factors?
    low=list[0] #get the first number
    high=list[number-1] #get the last number
    new=[high,low] #set up a new list
    return new #return the new list
blabla([1,2,3,4,5,6,7,8]) #example


# In[16]:


def bla(list): #define a function
    dododo=[] #set up a list
    for i in list: #start a cycle
        if i/2-int(i/2)==0: #for all factors in the given list,if it is even
            dododo.append(i)#then it should be added into the new list
    return dododo #retrun the new list
bla([3,45,23,43,43,4,12343,43,24]) #exapmle


# In[20]:


def blablabla(year): #define a function
    if year/4-int(year/4)==0: # if the year is leap
        print("True!!!") #then return True
blablabla(2000) #example


# In[23]:


a=input("what da you want to say?") #define a input variable
b=a.split() #divided the input into parts by " "
sentence = " ".join(b[::-1]) #reunion the parts in descending order
sentence #print it

