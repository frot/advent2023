#!/usr/bin/env python3

import fileinput
from collections import defaultdict

from math import prod
from igraph import Graph


def parse():
    nodes = defaultdict(set)
    for line in fileinput.input(encoding="utf-8"):
        ss = line.replace(':', '').split()
        nodes[ss[0]] |= set(ss[1:])
        for s in ss[1:]:
            nodes[s].add(ss[0])
    return nodes


def part1():
    nodes = parse()
    s1 = set(nodes)
    s2 = set()
    count = lambda v: len(nodes[v]-s1)
    while sum(map(count, s1)) != 3:
        n = max(s1, key=count)
        s1.remove(n)
        s2.add(n)
    return len(s1) * len(s2)


def part1b():
    nodes = parse()
    return prod(Graph.ListDict(nodes).mincut().sizes())


print(part1())
print(part1b())
