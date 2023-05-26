#!/usr/bin/env python
# coding: utf-8

# # Assignment 11 Solutions

# **SUBMITTED BY: PRAJWAL CHAUDHARY**

# #### 1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.

# In[1]:


spam = -33
assert spam >=0, 'Variable Spam should not be a -ve number'


# #### 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

# In[2]:


def raise_assert(egg,bacon):
    egg = egg.upper()
    bacon = bacon.upper()
    assert not(egg == bacon), 'Eggs/Bacon should not be same, which are same now'


# In[3]:


raise_assert('hello','HELLO')


# In[4]:


raise_assert('goodbye','GOODbye')


# #### 3. Create an assert statement that throws an AssertionError every time.

# In[5]:


def assert_always():
    assert False, 'Always Shows Assertion Error'
assert_always()


# #### 4. What are the two lines that must be present in your software in order to call logging.debug()?

# In[6]:


import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# #### 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

# In[7]:


import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Data Inserted Successfully")
logging.debug('Connection Closed Successfully')


# In[8]:


file = open("./application_log.txt","r")
for record in file.readlines():
    print(record)


# #### 6. What are the five levels of logging?
# **Ans:** The Five levels of Logging provided by Python's Logging Module are 
# **`CRITICAL(50)`**,
# **`ERROR(40)`**,
# **`WARNING(30)`**,
# **`INFO(20`**,
# **`DEBUG(10)`**,
# **`NOTSET(0)`**

# #### 7. What line of code would you add to your software to disable all logging messages?

# In[9]:


logging.disable = True


# #### 8.Why is using logging messages better than using print() to display the same message?
# **Ans:** Post devlopment of our code, we can disable logging messages without removing the logging function, whereas we need to
# manually remove print() statements, which would become a tedious activity. Also, print is used when we want to display any particular message or help whereas logging is used to record all events such as error, info, debug messages, timestamps.

# #### 9.What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
# **Ans:** The Differences between Step Over, Step In, Step Out buttons in debugger are:
# 1. Step in  -  Step In button will cause the debugger to execute the next line of code and then pause again.
# 2. Step Over - Step Over button will execute the next line of code, similar to the Step In button. However, if the next line of code is a function call, the Step Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns.         
# 3. Step out  - Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function. 

# #### 10.After you click Continue, when will the debugger stop ?
# **Ans:** This will cause the program to continue running normally, without pausing for debugging  untill it terminates or reaches a breakpoint.

# #### 11. What is the concept of a breakpoint?
# **Ans:** Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line

# In[ ]:




