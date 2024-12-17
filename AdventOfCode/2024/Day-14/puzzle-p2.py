import re
from copy import deepcopy


DAY = '14'
#NUM_COLS = 11
#NUM_ROWS = 7
NUM_COLS = 101
NUM_ROWS = 103

#coordinates are in (x, y) or (c, r) with + right and down.


def main():
    #filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        robot_list = [[int(x) for x in re.findall(r'-?\d+', line)] for line in f.read().splitlines()]

    seconds = 0
    #final_coordinates = list()
    #quadrant_counts = [0, 0]
    middle_col = (NUM_COLS // 2)
    max_symmetric = 0
    while True and seconds < 10000:
        seconds += 1
        final_coordinates = list()

        for c, r, cv, rv in robot_list:
            fc = int((c + (cv * seconds)) % (NUM_COLS * (cv/abs(cv))))
            if fc < 0:
                fc += NUM_COLS
            fr = int((r + (rv * seconds)) % (NUM_ROWS * (rv/abs(rv))))
            if fr < 0:
                fr += NUM_ROWS
            final_coordinates.append((fc, fr))


        # Look for l/r symmetry
        symmetric = 0
        for coord in final_coordinates:
            if (middle_col + (middle_col - coord[0]), coord[1]) in final_coordinates:
                symmetric += 1
        if symmetric > max_symmetric:
            max_symmetric = symmetric
            max_seconds = seconds
            print(f'At {max_seconds} seconds, the symmetry is {max_symmetric}')



if __name__ == '__main__':
    main()

#Answer = 7572        
