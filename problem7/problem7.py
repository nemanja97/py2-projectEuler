'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def sieve2(n):
    numbers = range(0,n)
    b = []
    for prime in numbers:
        if prime < 2:
            continue
        elif prime > n ** 0.5:
            break
        for i in range(prime ** 2, n, prime):
            numbers[i] = 0
    for x in numbers:
        if x > 1:
            b.append(x)
    return b
    #return [x for x in numbers if x > 1]

number = 1
a = sieve2(104750)
print a[-1]