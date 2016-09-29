# -*- coding: utf-8 -*-
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(number,terms=0):
    terms2 = terms
    if number == 1:
        return terms2
    if number % 2 == 0:
        number /= 2
        terms2 += 1
        return collatz(number,terms2)
    else:
        number = number * 3 + 1
        terms2 += 1
        return collatz(number,terms2)

max = 0
for num in range(1,1000001):
    testCase = collatz(num)
    if testCase > max:
        max = testCase
        num2 = num

print 'The max is for ', num2, 'at ', max, ' terms.'
