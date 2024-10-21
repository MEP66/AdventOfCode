from collections import Counter
from math import inf


DAY = '06'

MAX_SUM = 10000

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        map_points = [tuple(int(x) for x in line.split(', ')) for line in f.read().splitlines()]

    map_totals = dict.fromkeys(map_points, 0)

    c_min = min([c[0] for c in map_points])
    c_max = max([c[0] for c in map_points])
    r_min = min([r[1] for r in map_points])
    r_max = max([r[1] for r in map_points])

    dist_count = 0

    for c in range(c_min, c_max + 1):
        for r in range(r_min, r_max + 1):
            point_distances = dict()
            for col_in, row_in in map_points:
                point_distances[col_in, row_in] = abs(c-col_in) + abs(r-row_in)
            
            sum_dist = sum(point_distances.values())
            if sum_dist < MAX_SUM:
                dist_count += 1

    print(f'Max area: {dist_count}')


if __name__ == '__main__':
    main()

#Answer = 42513