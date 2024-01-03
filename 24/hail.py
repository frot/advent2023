#!/usr/bin/env python3

import fileinput
from sympy import Eq, solve, symbols


def parse():
    return [tuple(map(int, line.replace('@', ',').split(','))) for line in fileinput.input(encoding="utf-8")]


"""
y1 = ax + c
y2 = bx + d

c = y1 - ax
d = y2 - bx
"""


def part1(pmin=200000000000000, pmax=400000000000000):
    hh = parse()
    count = 0
    for i, (x1, y1, _, dx1, dy1, _) in enumerate(hh[:-1]):
        for x2, y2, _, dx2, dy2, _ in hh[i + 1:]:
            a = dy1 / dx1
            b = dy2 / dx2
            if a != b:
                c = y1 - a * x1
                d = y2 - b * x2
                x = (d - c) / (a - b)
                y = a * x + c
                if (pmin <= x <= pmax and
                        pmin <= y <= pmax and
                        (x > x1 if dx1 > 0 else x < x1) and
                        (x > x2 if dx2 > 0 else x < x2) and
                        (y > y1 if dy1 > 0 else y < y1) and
                        (y > y2 if dy2 > 0 else y < y2)):
                    count += 1
    return count


def part2():
    hh = parse()
    eq = []
    x, y, z, dx, dy, dz, t1, t2, t3 = symbols('x y z dx dy dz t1 t2 t3')
    t = t1, t2, t3
    for i, (x1, y1, z1, dx1, dy1, dz1) in enumerate(hh[:3]):
        eq.append(Eq(x + t[i] * dx, x1 + t[i] * dx1))
        eq.append(Eq(y + t[i] * dy, y1 + t[i] * dy1))
        eq.append(Eq(z + t[i] * dz, z1 + t[i] * dz1))
    s = solve(eq, [x, y, z, dx, dy, dz, t1, t2, t3])
    return sum(s[0][:3])


# print(part1(pmin=7, pmax=27))  # test_input
print(part1())
print(part2())
