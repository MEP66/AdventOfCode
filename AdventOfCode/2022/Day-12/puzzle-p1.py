# Helpful link:
# https://realpython.com/python-heapq-module/


from math import inf
from collections import namedtuple
import heapq

DAY = '12'
WEIGHTOFFSET = 97

Coord = namedtuple('Coord', ['r', 'c'])

stepdir = {'D': Coord(r=1, c=0), 'U': Coord(r=-1, c=0), 'R': Coord(r=0, c=1), 'L': Coord(r=0, c=-1)}

def is_valid(hmap, posold: Coord, posnew: Coord) -> bool:
    if not ((0 <= posnew.r < len(hmap)) and (0 <= posnew.c < len(hmap[0]))):
        return False
    
    # can go one up or unlimited down.
    if not ((hmap[posnew.r][posnew.c] - hmap[posold.r][posold.c]) <= 1):
        return False
    return True


def get_neighbors(hmap, current: Coord) -> Coord:
    for move in stepdir.values():
        position = Coord(current.r + move.r, current.c + move.c)
        if is_valid(hmap, current, position):
            yield position


def get_shorter_paths (tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path


def show_path(path, hmap):
    for r, c in path:
        hmap[c] = hmap[c][:r] + '@' + hmap[c][r + 1 :]
    return '\n'.join(hmap) + '\n'


def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    heightmatrix = []
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        rindex = 0
        while line:
            inputline = []
            for cindex, char in enumerate(line):
                if char == 'S':
                    inputline.append(0)
                    start = Coord(r=rindex, c=cindex)
                elif char == 'E':
                    inputline.append(ord('z') + 2 - ord('a'))
                    destination = Coord(r=rindex, c=cindex)
                else:
                    inputline.append(ord(char) - ord('a') + 1)
            heightmatrix.append(inputline)
            line = f.readline().strip()
            rindex += 1

    tentative = {start: []}
    candidates = [(0, start)]
    certain = set()

    while destination not in certain and len(candidates) > 0:
        _ignore, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(heightmatrix, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        print(len(tentative[destination]))
    else:
        raise ValueError('No path')

if __name__ == '__main__':
    main()

# Answer = 383
    