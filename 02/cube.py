#!/usr/bin/env python3

import fileinput


def tup(lc):
    w = {'red': 0, 'green': 0, 'blue': 0}
    for c in lc:
        n, col = c.split()
        w[col] += int(n)
    return tuple(w.values())


tot1 = 0
tot2 = 0
for line in fileinput.input(encoding="utf-8"):
    line = line.strip()
    g, l2 = line.split(':')
    num = int(g.split()[-1])
    sets = [tup(s.split(',')) for s in l2.split(';')]
    # Part 1
    if all(c[0] <= c[1] for s in sets for c in zip(s, (12, 13, 14))):
        tot1 += num
    # Part 2
    mcube = [0, 0, 0]
    for s in sets:
        for i in range(3):
            mcube[i] = max(mcube[i], s[i])
    p = mcube[0] * mcube[1] * mcube[2]
    tot2 += p

print(tot1)
print(tot2)
