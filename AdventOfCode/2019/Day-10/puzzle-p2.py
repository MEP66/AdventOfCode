from dataclasses import dataclass
from math import gcd, sqrt, atan2, copysign, pi
from collections import Counter
from itertools import groupby, cycle


DAY = '10'

TARGET_COUNT = 200

@dataclass
class Coord:
    c: int
    r: int


@dataclass
class Asteroid:
    cord: Coord
    slope: tuple()
    angle: float
    dist: float


def calc_loc_info(ast_from, ast_to) -> Asteroid:
    run = ast_to.c - ast_from.c
    rise = ast_to.r - ast_from.r
    if run == 0:
        rise = copysign(1, rise)
    elif rise == 0:
        run = copysign(1, run)
    else:
        s_gcd = gcd(rise, run)
        rise = int(rise/s_gcd)
        run = int(run/s_gcd)
    distance = sqrt(((ast_to.c - ast_from.c) ** 2) + ((ast_to.r - ast_from.r) ** 2))
    
    if rise == 0:
        if run > 0:
            angle_rad = pi/2
        else:
            angle_rad = 3*pi/2
    elif run == 0:
        if rise < 0:
            angle_rad = 0
        else:
            angle_rad = pi
    else:
        angle_rad = atan2((ast_to.r-ast_from.r), (ast_to.c-ast_from.c))+pi/2
        if angle_rad < 0:
            angle_rad += 2*pi

    return(Asteroid(cord = ast_to, slope = (rise, run), angle = round(angle_rad, 4), dist = round(distance, 4)
                    ))


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    all_coords = [Coord(c = col, r = row) for row, line in enumerate(input_data) for col, char in enumerate(line) if char == '#']

    max_visible = 0

    for coord_from in all_coords:
        remaining_coords = all_coords.copy()
        remaining_coords.remove(coord_from)
        slope_counter = Counter()

        for coord_to in remaining_coords:
            ast_data = calc_loc_info(coord_from, coord_to)
            slope_counter.update([ast_data.slope])

        if len(slope_counter) > max_visible:
            max_visible = len(slope_counter)
            best_coord = coord_from

    coord_from = best_coord
    remaining_coords = all_coords.copy()
    remaining_coords.remove(coord_from)
    all_asteroids = list()
   
    for coord_to in remaining_coords:
        ast_data = calc_loc_info(coord_from, coord_to)
        all_asteroids.append(ast_data)
    
    all_asteroids.sort(key=lambda v: (v.angle, v.dist))

    grouped_by_angle = [[k, list(g)] for k, g in groupby(all_asteroids, key=lambda f: f.angle)]

    count = 1
    for angle, asteroids in cycle(grouped_by_angle):
        if len(asteroids) > 0:
            if count == TARGET_COUNT:
                print(f'200th Asteroid to be vaporized is at: {asteroids[0]}')
                print(f'Answer = {asteroids[0].cord.c * 100 + asteroids[0].cord.r}')
                break
            else:
                asteroids.pop(0)
                count += 1
    pass


if __name__ == '__main__':
    main()

#Answer = 1919