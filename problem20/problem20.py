'''
Find the sum of the digits in the number 100!
'''

import math

a = str(math.factorial(100))
sum = 0

for i in range(0,len(a)):
    sum += int(a[i])

print sum