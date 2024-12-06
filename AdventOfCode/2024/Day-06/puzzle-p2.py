import copy


DAY = '06'


# Coordinates are in (x, y) or (c, r) with + right and down.

next_dir = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
step = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}


def move_forward(c, r, d, m):
    while True:
        newc = c + step[d][0]
        newr = r + step[d][1]
        if 0 <= newr < len(m[0]) and 0 <= newc < len(m):
            if not m[newr][newc]:
                return newc, newr, d
            else:
                d = next_dir[d]
        else:
            raise Exception("Off the grid")


def calc_map(p, d, m):
    ''' Given a start position, start direction, and object map,
    return wether or not this is a loop, and the path thorugh the map.'''

    c, r = p
    tiles_visited = {(c, r, d)}
    while True:
        try:
            c, r, d = move_forward(c, r, d, m)
            if (c, r, d) in tiles_visited:
                is_loop = True
                break
            tiles_visited.add((c, r, d))
        except:
            is_loop = False
            break
    path = set([(x[0], x[1]) for x in tiles_visited])
    return (is_loop, path)


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'

    obstacle_map = list()

    with open(filename, 'r', encoding='utf-8') as f:
        for ri, line in enumerate(f.read().splitlines()):
            obs_row = list()
            for ci, char in enumerate(line):
                if char == '^':
                    startpos = (ci, ri)
                    obs_row.append(False)
                elif char == '#':
                    obs_row.append(True)
                else:
                    obs_row.append(False)
            obstacle_map.append(obs_row)

    startdir = 'N'
    _, orig_path = calc_map(startpos, startdir, obstacle_map)

    newobs_map = copy.deepcopy(obstacle_map)
    num_loops = 0

    for obj_pos in orig_path:
        if obj_pos != startpos:
            newobs_map[obj_pos[1]][obj_pos[0]] = True
            is_loop, _ = calc_map(startpos, startdir, newobs_map)
            if is_loop:
                num_loops += 1
            newobs_map = copy.deepcopy(obstacle_map)

    print(f'Number of loops: {num_loops}')
    

if __name__ == '__main__':
    main()

#Answer = 1721