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

    closest = inf
    for intersection in intersections:
        closest = min(closest, abs(intersection[0]) + abs(intersection[1]))
        
    print(f'Closest intersecting point is: {closest}')


if __name__ == '__main__':
    main()

#Answer = 3229
