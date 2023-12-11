#!/usr/bin/env python3

import fileinput
import math


def part1():
    tot = 1
    with fileinput.input(encoding="utf-8") as fi:
        races = zip((int(n) for n in next(fi).split()[1:]), (int(n) for n in next(fi).split()[1:]))
        for t, d in races:
            x = math.floor(t/2-math.sqrt((t/2)**2 - d))
            n = t - 2*x - 1
            tot *= n
    return tot


def part2():
    with fileinput.input(encoding="utf-8") as fi:
        t = int(''.join(next(fi).split()[1:]))
        d = int(''.join(next(fi).split()[1:]))
        x = math.floor(t/2-math.sqrt((t/2)**2 - d))
        return t - 2*x - 1


print(part1())
print(part2())
