import sys
print(100/0)
try:
    print(100/0)  #ZeroDivisionError will be encountered here.
except:
    print(sys.exc_info()[1], 'Execption Occurred')   #This statement will be executed only if exception error found
else:
    print('No exeption occurred!!')
finally:
    print('Run this block of code always')   # This statement will be executed always
