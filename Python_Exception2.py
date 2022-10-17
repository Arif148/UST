import os
import sys

try:
    os.remove("E:/Python/test3.txt")   # FileNotFoundError will be encountered as test3.txt in not found in location
except:
    print("Below Exception Occurred")
    print(sys.exc_info()[1])

else:
    print('No Exception Occurred!')

finally:
    print('Run this block of code always.')
