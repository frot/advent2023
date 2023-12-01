#!/usr/bin/env python3

import fileinput

def num(line, r):
    for i in r:
        if line[i].isdigit():
            return line[i]
        if line[i] == "o":
            if line[i:].startswith("one"):
                return "1"
        elif line[i] == "t":
            if line[i:].startswith("two"):
                return "2"
            if line[i:].startswith("three"):
                return "3"
        elif line[i] == "f":
            if line[i:].startswith("four"):
                return "4"
            if line[i:].startswith("five"):
                return "5"
        elif line[i] == "s":
            if line[i:].startswith("six"):
                return "6"
            if line[i:].startswith("seven"):
                return "7"
        elif line[i] == "e":
            if line[i:].startswith("eight"):
                return "8"
        elif line[i] == "n":
            if line[i:].startswith("nine"):
                return "9"


s1=0
s2=0
for line in fileinput.input(encoding="utf-8"):
    line = line.strip()
    # Part 1
    d1 = [c for c in line if c.isdigit()]
    s1 += int(d1[0]+d1[-1])
    # Part 2
    n1 = num(line, range(0, len(line), 1))
    n2 = num(line, range(len(line)-1, -1, -1))
    s2 += int(n1 + n2)

print(s1)
print(s2)
