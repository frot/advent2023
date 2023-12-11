#!/usr/bin/env python3

import fileinput
from collections import Counter


CARDS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


# HANDS
# Five
# Four
# House
# Three
# Two pair
# Pair
# Card


def part1():
    hands = []
    for line in fileinput.input(encoding="utf-8"):
        h, b = line.split()
        hh = tuple(c for _, c in Counter(h).most_common(2))
        hands.append((hh, tuple(CARDS[c] for c in h), int(b)))
    hands.sort()
    return sum(n * b for n, (_, _, b) in enumerate(hands, start=1))


def part2():
    CARDS['J'] = 1  # J is now lowest
    hands = []
    for line in fileinput.input(encoding="utf-8"):
        h, b = line.split()
        h1 = h
        c1 = Counter(h1).most_common(2)
        if c1[0][1] < 5:
            if c1[0][0] == 'J':
                h1 = h1.replace('J', c1[1][0])
            else:
                h1 = h1.replace('J', c1[0][0])
        hh = tuple(c for _, c in Counter(h1).most_common(2))
        hands.append((hh, tuple(CARDS[c] for c in h), int(b)))
    hands.sort()
    return sum(n * b for n, (_, _, b) in enumerate(hands, start=1))


print(part1())
print(part2())
