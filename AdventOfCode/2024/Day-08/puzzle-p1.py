from collections import defaultdict
from itertools import combinations


DAY = '08'

#Coordinates are in (x, y) or (c, r) with + right and down.

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    ant_map = defaultdict(list)
    for ri, line in enumerate(input_data):
        for ci, char in enumerate(line):
            if char != '.':
                ant_map[char].append((ci, ri))

    last_row = len(input_data) - 1
    last_col = len(input_data[0]) - 1
    del(input_data)

    antinodes = set()
    for ant in ant_map.values():
        for ant_pairs in combinations(ant, 2):
            col_dist = ant_pairs[1][0] - ant_pairs[0][0]
            row_dist = ant_pairs[1][1] - ant_pairs[0][1]
            cx = ant_pairs[0][0] - col_dist
            rx = ant_pairs[0][1] - row_dist
            if 0 <= cx <= last_col and 0 <= rx <= last_row:
                antinodes.add((cx, rx))
                
            cx = ant_pairs[1][0] + col_dist
            rx = ant_pairs[1][1] + row_dist
            if 0 <= cx <= last_col and 0 <= rx <= last_row:
                antinodes.add((cx, rx))
    
    print(f'Total nodes: {len(antinodes)}')


if __name__ == '__main__':
    main()

#Answer = 379