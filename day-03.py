# https://adventofcode.com/2025/day/3

with open("input-03.txt") as f:
    batteries = [[int(n) for n in l[:-1]] for l in f.readlines()]

# Part 1:
s = 0
for b in batteries:
    digit_1 = max(b[:-1])
    digit_2 = max(b[b.index(digit_1)+1:])
    s += 10 * digit_1 + digit_2
print("Part 1: answer =", s)  # = 17085

# Part 2:
tot = 0
for b in batteries:
    jolt = 0
    leftovers = b
    for i in range(1,12):
        ith = max(leftovers[:-12+i])
        leftovers = leftovers[leftovers.index(ith)+1:]
        jolt = 10 * jolt + ith
    jolt = 10 * jolt + max(leftovers)
    tot += jolt
print("Part 2: answer =", tot) # = 169408143086082
