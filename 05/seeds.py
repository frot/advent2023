#!/usr/bin/env python3

import fileinput


def find_map1(s, m):
    for r in m:
        if s >= r[0] and s < (r[0]+r[2]):
            return r[1] + (s-r[0])
        if s < r[0]:
            break
    return s


def find_maps1(s, name, maps):
    tn, m = maps[name]
    sout = find_map1(s, m)
    if tn in maps:
        sout = find_maps1(sout, tn, maps)
    return sout


def part1():
    seeds = None
    name = None
    maps = {}
    with fileinput.input(encoding="utf-8") as fi:
        seeds = [int(s) for s in next(fi).split()[1:]]
        for line in fi:
            s1 = line.split()
            if len(s1) == 3:
                maps[name][1].append((int(s1[1]), int(s1[0]), int(s1[2])))
            elif len(s1) == 2:
                name, tn = s1[0].split('-to-')
                maps[name] = (tn, [])
            elif name:
                maps[name][1].sort()
        maps[name][1].sort()
    return min(find_maps1(s, 'seed', maps) for s in seeds)


def find_map2(s, m):
    out = []
    for r in m:
        if s[1] <= r[0]:
            break
        if (r[0]+r[2]) <= s[0]:
            continue
        if s[0] < r[0]:
            out += [(s[0], r[0])]
            s = (r[0], s[1])
        if s[1] > (r[0]+r[2]):
            out += [(r[1]+(s[0]-r[0]), r[1]+r[2])]
            s = (r[0]+r[2], s[1])
        else:
            s = (r[1]+(s[0]-r[0]), r[1]+(s[1]-r[0]))
            break
    return out + [s]


def find_maps2(ss, name, maps):
    tn, m = maps[name]
    sout = [si for s in ss for si in find_map2(s, m)]
    if tn in maps:
        sout = find_maps2(sout, tn, maps)
    return sorted(sout)


def part2():
    seeds = None
    name = None
    maps = {}
    with fileinput.input(encoding="utf-8") as fi:
        s1 = [int(s) for s in next(fi).split()[1:]]
        seeds = [(s1[i-1], s1[i-1]+s1[i]) for i in range(1, len(s1), 2)]
        for line in fi:
            s1 = line.split()
            if len(s1) == 3:
                maps[name][1].append((int(s1[1]), int(s1[0]), int(s1[2])))
            elif len(s1) == 2:
                name, tn = s1[0].split('-to-')
                maps[name] = (tn, [])
            elif name:
                maps[name][1].sort()
        maps[name][1].sort()
    return min(find_maps2([s], 'seed', maps)[0][0] for s in seeds)


print(part1())
print(part2())
