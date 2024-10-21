from collections import Counter
from math import inf


DAY = '06'

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

    for c in range(c_min, c_max + 1):
        for r in range(r_min, r_max + 1):
            point_distances = dict()
            for col_in, row_in in map_points:
                point_distances[col_in, row_in] = abs(c-col_in) + abs(r-row_in)
            min_dist = min(point_distances.values())
            dist_counts = Counter(point_distances.values())
            if dist_counts[min_dist] == 1:
                min_point = list(point_distances.keys())[list(point_distances.values()).index(min_dist)]
                if c not in (c_min, c_max) and r not in (r_min, r_max):
                    map_totals[min_point] += 1
                else:
                    map_totals[min_point] = inf

    final_totals = list(map_totals.values())
    while True:
        max_area = max(final_totals)
        if max_area == inf:
            final_totals.remove(max_area)
        else:
            print(f'Max area: {max_area}')
            break

if __name__ == '__main__':
    main()

#Answer = 5365