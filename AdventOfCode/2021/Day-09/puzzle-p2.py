

DAY = '09'

adjacents = ((-1, 0), (0, 1), (1, 0), (0, -1))

def get_basin_map(coord, fl_map, basin_map=None):
    if basin_map is None:
        basin_map = []
    
    r, c = coord
    if fl_map[r][c] == 9:
        return basin_map
    else:
        basin_map.append(coord)
    
    neighbors = list()
    for ra, ca in adjacents: 
        row_i = r + ra
        col_i = c + ca
        if 0 <= row_i < len(fl_map) and 0 <= col_i < len(fl_map[0]):
            if fl_map[row_i][col_i] > fl_map[r][c] and fl_map[row_i][col_i] != 9:
                neighbors.append((row_i, col_i))
    if neighbors:
        for nb in neighbors:
            nb_basin_map = get_basin_map(nb, fl_map, basin_map)
            basin_map = basin_map + nb_basin_map
    return list(set(basin_map))


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        floor_map = [[int(c) for c in line] for line in f.read().splitlines()]
    
    largest_basins = [0, 0, 0, 0]

    for ri, line in enumerate(floor_map):
        for ci, _ in enumerate(line):
            largest_basins[0] = len(get_basin_map((ri, ci), floor_map))
            largest_basins.sort()

    result = largest_basins[1] * largest_basins[2] * largest_basins[3]
    print(f'Prod of top 3 basins: {result}')
    

if __name__ == '__main__':
    main()

#Answer = 959136