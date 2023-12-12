#!/usr/bin/env python3

import fileinput


#  | is a vertical pipe connecting north and south.
#  - is a horizontal pipe connecting east and west.
#  L is a 90-degree bend connecting north and east.
#  J is a 90-degree bend connecting north and west.
#  7 is a 90-degree bend connecting south and west.
#  F is a 90-degree bend connecting south and east.
#  . is ground; there is no pipe in this tile.
#  S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


DIR = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0)),
}

START = {
    'ud': '|',
    'lr': '-',
    'ur': 'L',
    'ul': 'J',
    'dl': '7',
    'dr': 'F',
}

maze = []
dist = []


def parse():
    return [line.strip() for line in fileinput.input(encoding="utf-8")]


def find_start(m):
    for r, rr in enumerate(m):
        c = rr.find('S')
        if c >= 0:
            return r, c


def start_walk(r, c):
    global maze, dist
    dist[r][c] = 0
    sym = ''
    # Up
    if r > 0 and maze[r-1][c] in '|7F':
        sym += 'u'
        walk(r-1, c)
    # Down
    if r < len(maze)-1 and maze[r+1][c] in '|LJ':
        sym += 'd'
        walk(r+1, c)
    # Left
    if c > 0 and maze[r][c-1] in '-LF':
        sym += 'l'
        walk(r, c-1)
    # Right
    if c < len(maze[r])-1 and maze[r][c+1] in '-J7':
        sym += 'r'
        walk(r, c+1)
    maze[r] = maze[r].replace('S', START[sym])


def walk(r, c):
    global dist
    d = 1
    stack = []
    while True:
        if dist[r][c] == '.' or d < dist[r][c]:
            dist[r][c] = d
            stack.extend((r+rd, c+cd, d+1) for rd, cd in DIR[maze[r][c]])
        if stack:
            r, c, d = stack.pop()
        else:
            break


def part1():
    global maze, dist
    maze = parse()
    dist = [['.']*len(line) for line in maze]
    r, c = find_start(maze)
    start_walk(r, c)
    return max(col for row in dist for col in row if col != '.')


def part2():
    global maze, dist
    maze = parse()
    dist = [['.']*len(line) for line in maze]
    r, c = find_start(maze)
    start_walk(r, c)
    count = 0
    for mrow, drow in zip(maze, dist):
        inside = False
        last = '.'
        for mcol, dcol in zip(mrow, drow):
            if dcol == '.':
                if inside:
                    count += 1
            elif last == 'F' and mcol == 'J':
                last = mcol
            elif last == 'L' and mcol == '7':
                last = mcol
            elif mcol in '|LFJ7':
                last = mcol
                inside = not inside
    return count


print(part1())
print(part2())
