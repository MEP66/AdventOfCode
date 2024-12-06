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


def is_loop(p, d, m):
    c, r = p
    tiles_visited = set()
    tiles_visited.add((c, r, d))
    while True:
        try:
            c, r, d = move_forward(c, r, d, m)
            if (c, r, d) in tiles_visited:
                return True
            tiles_visited.add((c, r, d))
        except:
            return False

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

    nrows = len(obstacle_map)
    ncols = len(obstacle_map[0])
    newobs_map = copy.deepcopy(obstacle_map)
    num_loops = 0

    for ri in range(nrows):
        print(ri)
        for ci in range(ncols):
            if (ci, ri) != startpos and not newobs_map[ri][ci]:
                newobs_map[ri][ci] = True
                if is_loop(startpos, startdir, newobs_map):
                    num_loops += 1
                newobs_map = copy.deepcopy(obstacle_map)

    print(f'Number of loops: {num_loops}')
    

if __name__ == '__main__':
    main()

#Answer = 1721