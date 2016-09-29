'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

number = 600851475143
list_of_factors = []

for factor in range(int(math.sqrt(number)), 2, -1):
    if number % factor == 0:
        list_of_factors.append(factor)

for factor in list_of_factors:
    for prime in range(int(math.sqrt(factor)), 1, -1):
        isPrime = True
        if factor % prime == 0:
            isPrime = False
            break
    if isPrime == True:
        print factor
        break