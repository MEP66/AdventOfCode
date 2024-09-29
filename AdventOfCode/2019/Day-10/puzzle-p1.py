from dataclasses import dataclass
from math import gcd
from collections import Counter


DAY = '10'

@dataclass
class Coord:
    r: int
    c: int


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    all_coords = [Coord(r = row, c = col) for row, line in enumerate(input_data) for col, char in enumerate(line) if char == '#']

    max_visible = 0

    for coord_from in all_coords:
        remaining_coords = all_coords.copy()
        remaining_coords.remove(coord_from)
        slope_counter = Counter()

        for coord_to in remaining_coords:
            rise = coord_to.c - coord_from.c
            run = coord_to.r - coord_from.r
            if run == 0:
                rise = int(rise/abs(rise))
            elif rise == 0:
                run = int(run/abs(run))
            else:
                s_gcd = gcd(rise, run)
                rise = int(rise/s_gcd)
                run = int(run/s_gcd)
            slope_counter.update([(rise, run)])

        max_visible = max(max_visible, len(slope_counter))
    
    print(f'Max visible: {max_visible}')


if __name__ == '__main__':
    main()

#Answer = 247