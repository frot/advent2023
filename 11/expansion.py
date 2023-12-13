#!/usr/bin/env python3

import fileinput


def parse(rate):
    offset = 0
    galaxies = []
    cols = [0] * 140
    for r, line in enumerate(fileinput.input(encoding="utf-8")):
        line = line.strip()
        if '#' in line:
            for c, g in enumerate(line):
                if g == '#':
                    cols[c] += 1
                    galaxies.append((r + offset, c))
        else:
            offset += rate
    offset = 0
    for i, c in enumerate(cols):
        cols[i] = offset
        if c == 0:
            offset += rate
    galaxies = [(r, c + cols[c]) for r, c in galaxies]
    return galaxies


def partx(rate):
    tot = 0
    g = parse(rate)
    while g:
        g1 = g.pop()
        tot += sum(abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g2 in g)
    return tot


print(partx(1))
print(partx(999999))
