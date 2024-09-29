from math import inf

DAY = '03'


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        wires = [[(x[0], int(x[1:])) for x in line.split(',')] for line in f.read().splitlines()]

    move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    pos = (0, 0)
    wirepath1 = list()
    for dir, dist in wires[1]:
        for _ in range(dist):
            pos = tuple(map(lambda i, j: i + j, pos, move[dir]))
            wirepath1.append(pos)

    pos = (0, 0)
    moves2 = 0
    found = False
    for dir, dist in wires[0]:
        for _ in range(dist):
            pos = tuple(map(lambda i, j: i + j, pos, move[dir]))
            moves2 += 1
            if pos in wirepath1:
                moves1 = 0
                while pos != wirepath1[moves1]:
                    moves1 += 1
                moves1 += 1
                found = True
                break
        if found:
            break

    print(f'Minimum moves to intersection is: {moves2 + moves1}')


if __name__ == '__main__':
    main()

#Answer is not 82256, 32604