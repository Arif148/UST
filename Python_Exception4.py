import sys

# Raise Error if value of x exceeds 50
try:
    x = int(input('Enter First Number : '))
    if x > 50:
        raise ValueError(x)   # If value of x > 50 , valueError exception will be raised.
except:
    print(sys.exc_info()[0])

x = -10

if x < 0:
    raise Exception("No, numbers below zero is allowed!")

x = "Hello Python"

if not type(x) is int:
    raise TypeError("Only Integers are Allowed!")
