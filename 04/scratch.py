#!/usr/bin/env python3

import fileinput


def part1():
    tot = 0
    for i, line in enumerate(fileinput.input(encoding="utf-8")):
        s1 = line.split(':')[1].split('|')
        wn = {int(n) for n in s1[0].split()}
        yn = {int(n) for n in s1[1].split()}
        nums = wn & yn
        tot += int(2 ** (len(nums)-1))
    return tot


def part2():
    copies = [0] * 200
    for i, line in enumerate(fileinput.input(encoding="utf-8")):
        s1 = line.split(':')[1].split('|')
        wn = {int(n) for n in s1[0].split()}
        yn = {int(n) for n in s1[1].split()}
        nums = wn & yn
        copies[i] += 1
        for ii in range(i+1, i+len(nums)+1):
            copies[ii] += copies[i]
    return sum(copies)


print(part2())
