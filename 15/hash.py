#!/usr/bin/env python3

import fileinput


def calc_hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17
    return h % 256


def part1():
    return sum(calc_hash(step)
               for line in fileinput.input(encoding="utf-8")
               for step in line.strip().split(','))


def part2():
    boxes = [{} for i in range(256)]
    for line in fileinput.input(encoding="utf-8"):
        for step in line.strip().split(','):
            if '=' in step:
                h = calc_hash(step[:-2])
                boxes[h][step[:-2]] = int(step[-1])
            else:
                h = calc_hash(step[:-1])
                if step[:-1] in boxes[h]:
                    del boxes[h][step[:-1]]
    return sum(b * n * f
               for b, bb in enumerate(boxes, start=1)
               for n, f in enumerate(bb.values(), start=1))


print(part1())
print(part2())
