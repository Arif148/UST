# Handling Specific Exception
import os

try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x1/y)
    os.remove("E:/Python/text3.txt")

except NameError:
    print('NameError exception occurred')

except FileNotFoundError:
    print('FileNotFoundError exception occurred')

except ZeroDivisionError:
    print('ZeroDivisionError exception occurred')
