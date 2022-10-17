import os
import sys

# Key Error : This exception is raised when key does not exist in dictionary.
try:
    my_dict = {'id':102, 'name':'Suresh', 'city':'Bangalore', 'dept':'IT'}
    print(my_dict['name'])

except KeyError:
    print('KeyError Exception Raised.')


# Index Error - This exception is raised when an index of a sequence does not exist.
try:
    mylist = [1, 2, 3, 4, 5, 6]
    print(mylist[0])
    
except IndexError:
    print('IndexError Exception Raised')

# TypeError - This Exception is raised when two different data types are combined
try:
    a = 50
    b = 'Python'
    c = a / b

except TypeError:
    print('TypeError Exception Raised.')

