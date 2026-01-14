# https://adventofcode.com/2025/day/1

import numpy as np

with open("input-01.txt") as f:
    sign = {'L':-1, 'R':+1}
    steps = [sign[line[0]] * int(line[1:-1]) for line in f]

# Part 1:
starting_pos = 50
positions = np.cumsum([starting_pos] + steps) % 100

print("Part 1: answer =", np.sum(positions == 0)) # = 1021

# Part 2:
extra_turns = np.sum(np.abs(steps) // 100)  # |steps| > 100 contain extra turns

through_zero = np.sign(np.diff(positions)) != np.sign(steps)
through_zero |= positions[1:] == 0
through_zero &= positions[:-1] != 0  # true if the dial goes through zero when applying 
                                     # the step, without considering the extra turns.
print("Part 2: answer =", extra_turns + np.sum(through_zero)) # = 5933