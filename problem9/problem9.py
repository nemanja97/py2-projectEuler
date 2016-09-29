'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

while True:
    for a in range(1,1001):
        for b in range(a,1001):
            if (((1000 * (a + b) - a * b)) == 500000):
                print a * b * ((a ** 2 + b ** 2) ** 0.5)
                exit(0)
