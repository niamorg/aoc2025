# https://adventofcode.com/2025/day/2

import re

with open("input-02.txt") as f:
    ranges = [[int(n) for n in range.split('-')] for range in f.readline().split(',')]

def sum_matching_numbers(pattern):
    s = 0
    for a,b in ranges:
        for n in range(a, b+1):
            if bool(pattern.match(str(n))):
                s += n
    return s

# Part 1
pattern = re.compile(r'^(\d+)\1$')  # matches (D^+)^2 with D = {0, ..., 9}  (Formal language notation)
print("Part 1: answer =", sum_matching_numbers(pattern)) # = 12599655151

# Part 2
pattern = re.compile(r'^(\d+)\1+$')  # matches U_{n>=2} (D^+)^n
print("Part 2: answer =", sum_matching_numbers(pattern)) # = 20942028255