#!/usr/bin/env python3

import fileinput


memo = {}


def find(ss, gg):
    if (ss, gg) in memo:
        return memo[ss, gg]
    tmp = find1(ss, gg)
    memo[ss, gg] = tmp
    return tmp


def find1(ss, gg):
    if gg:
        g = gg[0]
        ss = ss.lstrip('.')
        if ss:
            if ss[0] == '?':
                return find(ss[1:], gg) + find('#' + ss[1:], gg)
            if len(ss) >= g and '.' not in ss[:g] and (len(ss) == g or ss[g] != '#'):
                return find(ss[g+1:], gg[1:])
        return 0
    return 0 if '#' in ss else 1


def part1():
    tot = 0
    for line in fileinput.input(encoding="utf-8"):
        s1, g1 = line.split()
        g2 = tuple(int(g) for g in g1.split(','))
        tot += find(s1, g2)
    return tot


def part2():
    tot = 0
    for line in fileinput.input(encoding="utf-8"):
        s1, g1 = line.split()
        g2 = tuple(int(g) for g in g1.split(','))
        tot += find('?'.join([s1]*5), g2*5)
    return tot


print(part1())
print(part2())
