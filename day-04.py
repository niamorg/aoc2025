# https://adventofcode.com/2025/day/4

import numpy as np
from scipy.signal import convolve2d

with open("input-04.txt") as f:
    rolls = np.array([[c == '@' for c in l] for l in f.readlines()], dtype=np.int8)

# Part 1:
neighbors_kernel = np.array([[1,1,1], [1,0,1], [1,1,1]], dtype=np.int8)
accessible = convolve2d(rolls, neighbors_kernel, mode='same') < 4
print("Part 1: answer =", np.sum(rolls & accessible)) # = 1441

# Part 2:
leftovers = np.copy(rolls)
while np.any(leftovers & (accessible := convolve2d(leftovers, neighbors_kernel, mode='same') < 4)):
    leftovers &= ~accessible   # removing accessible rolls until there are none
print("Part 2: answer =", np.sum(rolls) - np.sum(leftovers)) # = 9050