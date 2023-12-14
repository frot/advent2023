#!/usr/bin/env python3

import fileinput


def parse():
    return tuple(line.strip() for line in fileinput.input(encoding="utf-8"))


def weight(p, n):
    tot = 0
    for r in range(n):
        for c in range(n):
            if p[r][c] == 'O':
                tot += n - r
    return tot


def north(p, n):
    top = [0] * n
    for r in range(n):
        for c in range(n):
            if p[r][c] == 'O':
                p[r][c] = '.'
                p[top[c]][c] = 'O'
                top[c] += 1
            elif p[r][c] == '#':
                top[c] = r + 1


def south(p, n):
    top = [n-1] * n
    for r in range(n-1, -1, -1):
        for c in range(n):
            if p[r][c] == 'O':
                p[r][c] = '.'
                p[top[c]][c] = 'O'
                top[c] -= 1
            elif p[r][c] == '#':
                top[c] = r - 1


def west(p, n):
    top = [0] * n
    for c in range(n):
        for r in range(n):
            if p[r][c] == 'O':
                p[r][c] = '.'
                p[r][top[r]] = 'O'
                top[r] += 1
            elif p[r][c] == '#':
                top[r] = c + 1


def east(p, n):
    top = [n-1] * n
    for c in range(n-1, -1, -1):
        for r in range(n):
            if p[r][c] == 'O':
                p[r][c] = '.'
                p[r][top[r]] = 'O'
                top[r] -= 1
            elif p[r][c] == '#':
                top[r] = c - 1


memo = {}


def cycle(p, n):
        pp = [[c for c in r] for r in p]
        north(pp, n)
        west(pp, n)
        south(pp, n)
        east(pp, n)
        return tuple(''.join(r) for r in pp)


def part1():
    p = [[c for c in r] for r in parse()]
    n = len(p)
    north(p, n)
    return weight(p, n)


def part2():
    p_in = parse()
    n = len(p_in)
    for i in range(1000000000):
        if p_in in memo:
            ii, p_in = memo[p_in]
            i_out = ii + (1000000000 - i - 1) % (len(memo) - ii)
            p_in = list(memo.values())[i_out][1]
            break
        else:
            p = cycle(p_in, n)
            memo[p_in] = (i, p)
            p_in = p
    return weight(p_in, n)


print(part1())
print(part2())
