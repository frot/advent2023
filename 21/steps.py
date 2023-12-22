#!/usr/bin/env python3

import fileinput


def parse():
    m = [line.strip() for line in fileinput.input(encoding="utf-8")]
    s = set((r, c) for r, row in enumerate(m) for c, col in enumerate(row) if col == 'S')
    return m, s


def step(m, s):
    o = set()
    w = len(m)
    for r, c in s:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r1 = r + dr
            c1 = c + dc
            if m[r1 % w][c1 % w] != '#':
                o.add((r1, c1))
    return o


def count(m, e, n):
    e_new = e
    counts = [0] * n
    counts[-1] = 1
    for i in range(n):
        e_new = step(m, e_new) - e
        e |= e_new
        counts[i] = counts[i - 2] + len(e_new)
    return [1] + counts


def part1(n=64):
    m, e = parse()
    return count(m, e, n)[n]


def part2(n=26501365):
    m, e = parse()
    w = len(m)
    r = n % w
    c = count(m, e, r + w)

    y1, y2, y3 = c[w - r - 2], c[r], c[r + w]
    a = (y3 + y1) // 2 - y2
    b = (y3 - y1) // 2
    c = y2
    x = n // w

    return a * x**2 + b * x + c


print(part1())
print(part2())
