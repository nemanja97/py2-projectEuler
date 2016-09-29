'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def sieve_sum_of_primes(n):
    numbers = range(0,n)
    sum = 0
    for prime in numbers:
        if prime < 2:
            continue
        elif prime > n ** 0.5:
            break
        for i in range(prime ** 2, n, prime):
            numbers[i] = 0
    for x in numbers:
        if x > 1:
            sum += x
    return sum

print sieve_sum_of_primes(2000000)
