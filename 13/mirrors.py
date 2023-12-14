#!/usr/bin/env python3

import fileinput


def transpose(p):
    t = [''] * len(p[0])
    for r in p:
        for i, c in enumerate(r):
            t[i] += c
    return t


def parse():
    pp = []
    p = []
    for line in fileinput.input(encoding="utf-8"):
        line = line.strip()
        if line:
            p.append(line)
        else:
            pp.append((p, transpose(p)))
            p = []
    pp.append((p, transpose(p)))
    return pp


def find(p):
    for r in range(1, len(p)):
        if p[r-1] == p[r]:
            n = min(r, len(p)-r)
            if all(p[r-1-i] == p[r+i] for i in range(1, n)):
                return r
    return 0


errcount = 0


def check(aa, bb):
    global errcount
    s = sum(1 for a, b in zip(aa, bb) if a != b)
    if s == 0:
        return True
    if s == errcount:
        errcount = 0
        return True
    return False


def find2(p, r0):
    global errcount
    for r in range(1, len(p)):
        errcount = 1
        if r != r0 and check(p[r-1], p[r]):
            n = min(r, len(p)-r)
            if all(check(p[r-1-i], p[r+i]) for i in range(1, n)):
                return r
    return 0


def part1():
    tot = 0
    for p in parse():
        tot += 100 * find(p[0])
        tot += find(p[1])
    return tot


def part2():
    tot = 0
    for p in parse():
        tot += 100 * find2(p[0], find(p[0]))
        tot += find2(p[1], find(p[1]))
    return tot


print(part1())
print(part2())
