#!/usr/bin/env python3

import fileinput
from collections import defaultdict


def parse():
    m = sorted(tuple(sorted(tuple(int(s2) for s2 in reversed(s1.split(',')))
                     for s1 in line.strip().split('~')) + [fileinput.lineno()])
               for line in fileinput.input(encoding="utf-8"))
    return m


def count(ch, pa, nn, s):
    for n in nn:
        if pa[n] <= s:
            s.add(n)
            if n in ch:
                count(ch, pa, ch[n], s)


def compact(mm):
    tops = defaultdict(lambda: (0, 0))
    locked = defaultdict(set)
    supports = defaultdict(set)
    supported = defaultdict(set)
    for i, ((z1, y1, x1), (z2, y2, x2), n) in enumerate(mm):
        z = max(tops[(y, x)][0] for y in range(y1, y2 + 1) for x in range(x1, x2 + 1))
        ss = {tops[(y, x)][1] for y in range(y1, y2 + 1) for x in range(x1, x2 + 1) if tops[(y, x)][0] == z and tops[(y, x)][1]}
        for s in ss:
            supports[s].add(n)
            supported[n].add(s)
        if len(ss) == 1:
            locked[ss.pop()].add(n)
        z += 1 + z2 - z1
        mm[i] = ((z, y1, x1), (z, y2, x2), n)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                tops[(y, x)] = (z, n)

    free = len(set(m[2] for m in mm) - set(locked.keys()))
    tot = 0
    for k, v in locked.items():
        s = set([k])
        count(supports, supported, v, s)
        tot += len(s) - 1
    return free, tot


def part1():
    m = parse()
    return compact(m)


# 92108 too high
print(part1())
