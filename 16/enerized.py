#!/usr/bin/env python3

import fileinput


def parse():
    return [line.strip() for line in fileinput.input(encoding="utf-8")]


def part1(mm, r=0, c=0, dr=0, dc=1):
    bb = [(r, c, dr, dc)]
    s1 = set()
    s2 = set()
    while bb:
        r, c, dr, dc = bb.pop()
        if r < 0 or r >= len(mm) or c < 0 or c >= len(mm):
            continue
        if (r, c, dr, dc) in s1:
            continue
        s1.add((r, c, dr, dc))
        s2.add((r, c))
        p = mm[r][c]
        if p == '\\':
            bb.append((r+dc, c+dr, dc, dr))
        elif p == '/':
            bb.append((r-dc, c-dr, -dc, -dr))
        elif p == '|' and dc != 0:
            bb.append((r-1, c, -1, 0))
            bb.append((r+1, c, 1, 0))
        elif p == '-' and dr != 0:
            bb.append((r, c-1, 0, -1))
            bb.append((r, c+1, 0, 1))
        else:
            bb.append((r+dr, c+dc, dr, dc))
    return len(s2)


def part2(mm):
    pp = []
    for r in range(len(mm)):
        pp.append(part1(mm, r, 0, 0, 1))
        pp.append(part1(mm, r, len(mm)-1, 0, -1))
    for c in range(len(mm)):
        pp.append(part1(mm, 0, c, 1, 0))
        pp.append(part1(mm, len(mm)-1, c, -1, 0))
    return max(pp)


print(part1(parse()))
print(part2(parse()))
