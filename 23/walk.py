#!/usr/bin/env python3

import sys
import fileinput
sys.setrecursionlimit(1000000)


D = ((0, -1, '<'), (0, 1, '>'), (-1, 0, '^'), (1, 0, 'v'))


def parse():
    return [line.strip() for line in fileinput.input(encoding="utf-8")]


lon = 0


def walk(mm, vv, r, c, s):
    global lon
    vv.add((r, c))
    for dr, dc, dd in D:
        r1 = r + dr
        c1 = c + dc
        if 0 <= r1 < len(mm) and 0 <= c1 < len(mm[0]) and mm[r1][c1] != '#':  # and (mm[r][c] == '.' or mm[r][c] == dd):
            if r1 == len(mm) - 1:
                lon = max(lon, s + 1)
                print(lon)
            elif (r1, c1) not in vv:
                walk(mm, vv, r1, c1, s + 1)
    vv.discard((r, c))
    return lon


# Part 2 optimizations
# Generate weighted graph first


def part1():
    mm = parse()
    return walk(mm, set(), 0, 1, 0)


print(part1())
