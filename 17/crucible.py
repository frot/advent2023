#!/usr/bin/env python3

import fileinput
from queue import PriorityQueue


def parse():
    return [[int(c) for c in line.strip()] for line in fileinput.input(encoding="utf-8")]


def part1(mm):
    e = len(mm)-1
    bb = PriorityQueue()
    bb.put((0, 0, 0, 0, 0))
    bb.put((0, 0, 1, 0, 0))
    s1 = {
        (0, 0, 0, 0): 0,
        (0, 1, 0, 0): 0
    }
    while bb:
        _, d, p, r, c = bb.get()
        if (r, c) == (e, e):
            return s1[(d, p, r, c)]
        if r > 0 and p != 1 and (p != 3 or d < 3):
            d2 = d + 1 if p == 3 else 1
            p2 = 3
            r2 = r - 1
            c2 = c
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))
        if c > 0 and p != 0 and (p != 2 or d < 3):
            d2 = d + 1 if p == 2 else 1
            p2 = 2
            r2 = r
            c2 = c - 1
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))
        if r < e and p != 3 and (p != 1 or d < 3):
            d2 = d + 1 if p == 1 else 1
            p2 = 1
            r2 = r + 1
            c2 = c
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))
        if c < e and p != 2 and (p != 0 or d < 3):
            d2 = d + 1 if p == 0 else 1
            p2 = 0
            r2 = r
            c2 = c + 1
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))


def part2(mm):
    e = len(mm)-1
    bb = PriorityQueue()
    bb.put((0, 0, 0, 0, 0))
    bb.put((0, 0, 1, 0, 0))
    s1 = {
        (0, 0, 0, 0): 0,
        (0, 1, 0, 0): 0
    }
    while bb:
        _, d, p, r, c = bb.get()
        if (r, c) == (e, e):
            return s1[(d, p, r, c)]
        if r > 0 and ((p in [0, 2] and d > 3) or (p == 3 and d < 10)):
            d2 = d + 1 if p == 3 else 1
            p2 = 3
            r2 = r - 1
            c2 = c
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))
        if c > 0 and ((p in [1, 3] and d > 3) or (p == 2 and d < 10)):
            d2 = d + 1 if p == 2 else 1
            p2 = 2
            r2 = r
            c2 = c - 1
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))
        if r < e and ((p in [0, 2] and d > 3) or (p == 1 and d < 10)):
            d2 = d + 1 if p == 1 else 1
            p2 = 1
            r2 = r + 1
            c2 = c
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))
        if c < e and ((p in [1, 3] and d > 3) or (p == 0 and d < 10)):
            d2 = d + 1 if p == 0 else 1
            p2 = 0
            r2 = r
            c2 = c + 1
            h2 = s1[(d, p, r, c)] + mm[r2][c2]
            if (d2, p2, r2, c2) not in s1 or h2 < s1[(d2, p2, r2, c2)]:
                s1[(d2, p2, r2, c2)] = h2
                bb.put((h2, d2, p2, r2, c2))


print(part1(parse()))
print(part2(parse()))
