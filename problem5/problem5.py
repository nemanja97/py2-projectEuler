'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

number = 20

while True:
    if (number % 20 == 0) and (number % 19 == 0) and (number % 18 == 0) and (number % 17 == 0) and (number % 16 == 0) \
    and (number % 15 == 0) and (number % 14 == 0) and (number % 13 == 0) and (number % 14 == 0) and (number % 13 == 0) \
    and (number % 12 == 0) and (number % 11 == 0):
        print number
        exit(0)
    number += 1