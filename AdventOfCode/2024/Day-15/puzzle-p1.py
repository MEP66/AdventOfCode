

DAY = '15'


# Coordinates are in (x, y) or (c, r) format, with + down and right.

move_dir = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}


def move_obj(d, c, fmap):
    cc = c[0]
    cr = c[1]
    nc = cc + move_dir[d][0]
    nr = cr + move_dir[d][1]

    match fmap[nr][nc]:
        case '#':
            return (False, c)
        case 'O':
            was_moved, _ = move_obj(d, (nc, nr), fmap)
            if was_moved:
                fmap[nr][nc] = fmap[cr][cc]
                fmap[cr][cc] = '.'
                return (True, (nc, nr))
            else:
                return (False, c)
        case '.':
            fmap[nr][nc] = fmap[cr][cc]
            fmap[cr][cc] = '.'
            return (True, (nc, nr))
        

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[x for x in line] for line in f.read().splitlines()]

    for ri, line in enumerate(input_data):
        if not line:
            break
   
    floor_map = input_data[:ri]
    
    instructions = list()
    for line in input_data[ri+1:]:
        instructions.extend(line)

    del input_data

    for ri, row in enumerate(floor_map):
        for ci, obj in enumerate(row):
            if obj == '@':
                robot_loc = [ci, ri]
                break
        else:
            continue
        break

    for move in instructions:
        _, new_loc = move_obj(move, robot_loc, floor_map)
        robot_loc = new_loc

    sum_gps = 0
    for ri, row in enumerate(floor_map):
        for ci, obj in enumerate(row):
            if obj == 'O':
                sum_gps += 100 * ri + ci
    
    print(f'GPS sum = {sum_gps}')

if __name__ == '__main__':
    main()

#Answer = 1371036