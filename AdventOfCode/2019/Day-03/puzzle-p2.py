from math import inf

DAY = '03'


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        wires = [[(x[0], int(x[1:])) for x in line.split(',')] for line in f.read().splitlines()]

    wpaths = list()

    move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    for wire in wires:
        pos = (0, 0)
        wirepath = set()
        for dir, dist in wire:
            for _ in range(dist):
                pos = tuple(map(lambda i, j: i + j, pos, move[dir]))
                wirepath.add(pos)
        wpaths.append(wirepath)
        
    intersections = wpaths[0].intersection(wpaths[1])

    steps_dict = dict()
    for i in intersections:
        steps_dict[i] = 0

    for wire in wires:
        visited = set()
        pos = (0, 0)
        steps = 0
        for dir, dist in wire:
            for _ in range(dist):
                pos = tuple(map(lambda i, j: i + j, pos, move[dir]))
                steps += 1
                if pos in intersections and pos not in visited:
                    visited.add(pos)
                    steps_dict[pos] += steps

    closest = min(steps_dict.values())

    print(f'Closest combibed steps is: {closest}')


if __name__ == '__main__':
    main()

#Answer = 32132
