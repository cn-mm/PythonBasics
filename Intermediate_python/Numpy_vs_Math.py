import timeit

# Set random values for our variables.
setup = """
import random
b1x = random.randrange(0, 800)
b1y = random.randrange(0, 600)
b2x = random.randrange(0, 800)
b2y = random.randrange(0, 600)
"""

math = """math.sqrt((b2x - b1x)**2 + (b2y - b1y)**2)"""
np = """numpy.linalg.norm(numpy.array([b1x, b1y]) - numpy.array([b2x, b2y]))"""

print('Math: ', timeit.timeit(math, setup='\n'.join(['import math', setup]), number=100000))
print('Numpy:', timeit.timeit(np, setup='\n'.join(['import numpy', setup]), number=100000))

# Math operates 10 times faster here but numpy works better when numpy arrays are being used
