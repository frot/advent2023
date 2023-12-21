#!/usr/bin/env python3

import fileinput
import re
import math
from queue import Queue


def parse():
    conf = {}
    for line in fileinput.input(encoding="utf-8"):
        m = re.match(r'([%&]?)(\w+) -> (.*)', line)
        conf[m[2]] = (m[1], m[3].split(', '), {})
    for k, n1 in conf.items():
        for n in n1[1]:
            if n in conf:
                n2 = conf[n]
                if n2[0] == '%':
                    n2[2]['%'] = False
                elif n2[0] == '&':
                    n2[2][k] = False
    return conf


def part1():
    conf = parse()
    q = Queue()
    count_low = 0
    count_high = 0
    for i in range(1000):
        q.put(('button', 'broadcaster', False))
        count_low += 1
        while not q.empty():
            frm, name, signal = q.get()
            if name not in conf:
                continue
            mt, outs, state = conf[name]
            if mt == '%':
                if signal:
                    continue
                state['%'] = not state['%']
                signal = state['%']
            elif mt == '&':
                state[frm] = signal
                signal = not all(s for s in state.values())
            for node in outs:
                q.put((name, node, signal))
                if signal:
                    count_high += 1
                else:
                    count_low += 1
    return count_low * count_high


def part2(end='nc'):
    conf = parse()
    q = Queue()
    i = 0
    count = {k: 0 for k, v in conf.items() if end in v[1]}
    while True:
        q.put(('button', 'broadcaster', False))
        i += 1
        while not q.empty():
            frm, name, signal = q.get()
            if name not in conf:
                continue
            mt, outs, state = conf[name]
            if mt == '%':
                if signal:
                    continue
                state['%'] = not state['%']
                signal = state['%']
            elif mt == '&':
                state[frm] = signal
                signal = not all(s for s in state.values())
            for node in outs:
                q.put((name, node, signal))
                if signal and name in count:
                    count[name] = i
                    if all(v for v in count.values()):
                        nn = list(count.values())
                        for n in nn[:-1]:
                            d = math.gcd(n, nn[-1])
                            nn[-1] = n * nn[-1] // d
                        return nn[-1]


print(part1())
print(part2())
