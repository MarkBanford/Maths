from numpy import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000000  # darts thrown

circlex = []
circley = []

squarex = []
squarey = []

r = 1

i = 1

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # specify those darts in cirlce

    if (x ** 2 + y ** 2 <= r ** 2):  # if dart in circle
        circlex.append(x)
        circley.append(y)
    else:  # if not in circle
        squarex.append(x)
        squarey.append(y)
    i += 1

pi = 4 * len(circlex) / float(N)

print(f'Pi is approximately {pi:5f}')

plt.plot(circlex, circley, 'b.')
plt.plot(squarex, squarey, 'g.')
plt.grid()
plt.show()
