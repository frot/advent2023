#!/usr/bin/env python3

import fileinput


def predict(nums):
    n2 = [nums[i]-nums[i-1] for i in range(1, len(nums))]
    if any(n != 0 for n in n2):
        prv, nxt = predict(n2)
        return nums[0] - prv, nums[-1] + nxt
    return nums[0], nums[-1]


def part1():
    tot = 0
    for line in fileinput.input(encoding="utf-8"):
        tot += predict([int(n) for n in line.split()])[1]
    return tot


def part2():
    tot = 0
    for line in fileinput.input(encoding="utf-8"):
        tot += predict([int(n) for n in line.split()])[0]
    return tot


print(part1())
print(part2())
