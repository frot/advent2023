#!/usr/bin/env python3

import fileinput
from collections import defaultdict


def parse():
    rules = defaultdict(list)
    parts = []
    with fileinput.input(encoding="utf-8") as fi:
        for line in fi:
            line = line.strip()
            if line:
                s = line.split('{')
                for r in s[1][:-1].split(','):
                    if ':' in r:
                        rules[s[0]].append(tuple(r.split(':')))
                    else:
                        rules[s[0]].append(('True', r))
            else:
                break
        for line in fi:
            parts.append({k: int(v) for k, v in (p.split('=') for p in line[1:-2].split(','))})
    return rules, parts


def accepted(part, rules):
    rr = rules['in']
    while True:
        for r in rr:
            if eval(r[0], None, part):
                if r[1] == 'A':
                    return True
                if r[1] == 'R':
                    return False
                rr = rules[r[1]]
                break


def part1():
    rules, parts = parse()
    return sum(sum(p.values()) for p in parts if accepted(p, rules))


def split_lt(pp, n):
    p1 = []
    p2 = []
    for p in pp:
        if p[0] < n:
            if p[1] < n:
                p1.append(p)
            else:
                p1.append((p[0], n - 1))
                p2.append((n, p[1]))
        else:
            p2.append(p)
    return p1, p2


def split_gt(pp, n):
    p1 = []
    p2 = []
    for p in pp:
        if p[1] > n:
            if p[0] > n:
                p1.append(p)
            else:
                p1.append((n + 1, p[1]))
                p2.append((p[0], n))
        else:
            p2.append(p)
    return p1, p2


def combinations(parts):
    count = 1
    for v in parts.values():
        count *= (1 + v[0][1] - v[0][0])
    return count


def walk(rules, name, parts):
    if name == 'R':
        return 0
    if name == 'A':
        return combinations(parts)

    count = 0
    parts = parts.copy()
    for (rcond, rdest) in rules[name]:
        cat = rcond[0]
        if rcond[1] in '<>':
            if rcond[1] == '<':
                (p1, p2) = split_lt(parts[cat], int(rcond[2:]))
            else:
                (p1, p2) = split_gt(parts[cat], int(rcond[2:]))
            if p1:
                parts[cat] = p1
                count += walk(rules, rdest, parts)
            if not p2:
                break
            parts[cat] = p2
        else:
            count += walk(rules, rdest, parts)

    return count


def part2():
    rules, _ = parse()
    return walk(rules, 'in', {'x': [(1, 4000)], 'm': [(1, 4000)], 'a': [(1, 4000)], 's': [(1, 4000)]})


print(part1())
print(part2())
