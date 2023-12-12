#!/usr/bin/env python3

import fileinput
import math


def parse():
    with fileinput.input(encoding="utf-8") as fi:
        instr = next(fi).strip()
        next(fi)
        nodes = {}
        for line in fi:
            n, _, le, ri = line.split()
            nodes[n] = (le[1:4], ri[0:3])
    return instr, nodes


def part1():
    instr, nodes = parse()
    steps = 0
    n = 'AAA'
    while True:
        for i in instr:
            steps += 1
            if i == 'L':
                n = nodes[n][0]
            else:
                n = nodes[n][1]
            if n == 'ZZZ':
                return steps


def loops(instr, nodes, n):
    steps = 0
    while True:
        for i in instr:
            steps += 1
            if i == 'L':
                n = nodes[n][0]
            else:
                n = nodes[n][1]
            if n[-1] == 'Z':
                return steps


def part2():
    instr, nodes = parse()
    nn = [loops(instr, nodes, k) for k in nodes.keys() if k[-1] == 'A']
    while len(nn) > 1:
        n1 = nn.pop()
        n2 = nn[-1]
        d = math.gcd(n1, n2)
        nn[-1] = n1*n2 // d
    return nn[0]


print(part1())
print(part2())
