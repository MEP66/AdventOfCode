

DAY = '11'


look = {'n': (0, -1), 'ne': (1, -1), 'e': (1, 0),
        'se': (1, 1), 's': (0, 1), 'sw': (-1, 1),
        'w': (-1, 0), 'nw': (-1, -1)}


def occupied_neighbors(coord, smap):
    tosum = list()
    for dir in look:
        exam_x, exam_y = coord
        while True:
            exam_x += look[dir][0]
            exam_y += look[dir][1]
            if ((0 <= exam_x < len(smap[0])) and (0 <= exam_y < len(smap))):
                seat = smap[exam_y][exam_x]
                if seat != '.':
                    tosum.append(seat)
                    break
            else:
                break
    return sum(tosum)


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    seat_map = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for row in f.read().splitlines():
            rowlist = list()
            for seat in row:
                match seat:
                    case 'L':
                        rowlist.append(0)
                    case '#':
                        rowlist.append(1)
                    case '.':
                        rowlist.append('.')
            seat_map.append(rowlist)

    while True:
        arrival_map = [['.' for _ in range(len(seat_map[0]))] for _ in range(len(seat_map))]
        change = False
        for y, row in enumerate(seat_map):
            for x, seat in enumerate(row):
                match seat:
                    case 1:
                        if occupied_neighbors((x, y), seat_map) >= 5:
                            arrival_map[y][x] = 0
                            change = True
                        else:
                            arrival_map[y][x] = 1
                    case 0:
                        if occupied_neighbors((x, y), seat_map) == 0:
                            arrival_map[y][x] = 1
                            change = True
                        else:
                            arrival_map[y][x] = 0
                    case '.':
                        arrival_map[y][x] = '.'
        seat_map = arrival_map.copy()
        if change == False:
            break

    tl = [0, 0]
    br = [len(seat_map[0]), len(seat_map)]
    occupied_seats = [seat_map[y][x] for y in range(tl[1], br[1])
                        for x in range(tl[0], br[0])
                        if seat_map[y][x] != '.']
    print (f'Occupied seats: {sum(occupied_seats)}')


if __name__ == '__main__':
    main()

#Answer = 1974