

DAY = '06'


# Coordinates are in (x, y) or (c, r) with + right and down.

next_dir = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
step = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

def move_forward(p, d, m):
    c, r = p
    while True:
        newp = [c + step[d][0], r + step[d][1]]
        if newp[1] < 0 or newp[0] < 0:
            raise Exception("Off the grid")
        if m[newp[1]][newp[0]] != '#':
            return newp, d
        else:
            d = next_dir[d]

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        lab_map = [[c for c in line] for line in f.read().splitlines()]

    for ri, row in enumerate(lab_map):
        for ci, tile in enumerate(row):
            if tile == '^':
                pos = [ci, ri]
                dir = 'N'
                
    tiles_visited = set()
    tiles_visited.add(tuple(pos))

    while True:
        try:
            pos, dir = move_forward(pos, dir, lab_map)
            tiles_visited.add(tuple(pos))
        except:
            break
    
    print(f'Number of positions visited: {len(tiles_visited)}')
    

if __name__ == '__main__':
    main()

#Answer = 4826