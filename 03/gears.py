#!/usr/bin/env python3

import fileinput
import re


RE = re.compile(r'[0-9]+')


def sym(cc):
    return any(c not in '.0123456789\n' for c in cc)


def part1():
    tot = 0
    mm = [[]]
    last_line = '.' * 150
    for line in fileinput.input(encoding="utf-8"):
        mm.append(list(RE.finditer(line)))
        for m in re.finditer('[^0-9.\n]', last_line):
            nums = [int(n[0]) for n in mm[-1]+mm[-2]+mm[-3] if n.end() >= m.start() and n.start() <= m.end()]
            tot += sum(nums)
        last_line = line
    return tot


def part2():
    tot = 0
    mm = [[]]
    last_line = '.' * 150
    for line in fileinput.input(encoding="utf-8"):
        mm.append(list(RE.finditer(line)))
        for m in re.finditer(r'\*', last_line):
            nums = [int(n[0]) for n in mm[-1]+mm[-2]+mm[-3] if n.end() >= m.start() and n.start() <= m.end()]
            if len(nums) == 2:
                tot += nums[0] * nums[1]
        last_line = line
    return tot


print(part2())
