#!/usr/bin/env python3

import fileinput


def pl1(s):
    return s[0], int(s[1])


def pl2(s):
    d = ['R', 'D', 'L', 'U']
    return d[int(s[2][7:8])], int(s[2][2:7], 16)


def parse(pl):
    a = 0
    r1, c1, r2, c2 = 0, 0, 0, 0
    for line in fileinput.input(encoding="utf-8"):
        direction, dist = pl(line.split())
        if direction == 'U':
            r2 = r1 - dist
        elif direction == 'D':
            r2 = r1 + dist
        elif direction == 'L':
            c2 = c1 - dist
        elif direction == 'R':
            c2 = c1 + dist
        a += r1*c2 - r2*c1 - dist
        r1, c1 = r2, c2
    return 1 + abs(a//2)


def part1():
    return parse(pl1)


def part2():
    return parse(pl2)


print(part1())
print(part2())
