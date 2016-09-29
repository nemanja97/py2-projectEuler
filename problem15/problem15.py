# -*- coding: utf-8 -*-
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

import math

gridSize = 20

# n!/r!(n-r)!
routes = (math.factorial(2*gridSize))/(math.factorial(gridSize)*math.factorial((gridSize*2-gridSize)))
print routes