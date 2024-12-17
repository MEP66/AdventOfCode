import re


DAY = '14'
#NUM_COLS = 11
#NUM_ROWS = 7
NUM_COLS = 101
NUM_ROWS = 103

#coordinates are in (x, y) or (c, r) with + right and down.

SECONDS = 100

def main():
    #filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        robot_list = [[int(x) for x in re.findall(r'-?\d+', line)] for line in f.read().splitlines()]

    final_coordinates = list()
    quadrant_counts = [0, 0, 0, 0]
    middle_col = (NUM_COLS // 2)
    middle_row = (NUM_ROWS // 2)
    for c, r, cv, rv in robot_list:
        fc = int((c + (cv * SECONDS)) % (NUM_COLS * (cv/abs(cv))))
        if fc < 0:
            fc += NUM_COLS
        fr = int((r + (rv * SECONDS)) % (NUM_ROWS * (rv/abs(rv))))
        if fr < 0:
            fr += NUM_ROWS
        final_coordinates.append((fc, fr))
        if fr < middle_row:
            if fc < middle_col:
                quadrant_counts[0] += 1
            elif fc > middle_col:
                quadrant_counts[1] += 1
        elif fr > middle_row:
            if fc < middle_col:
                quadrant_counts[2] += 1
            elif fc > middle_col:
                quadrant_counts[3] += 1
    
    saftey_factor = 1
    for q in quadrant_counts:
        saftey_factor *= q

    print(f'Saftey factor = {saftey_factor}')


if __name__ == '__main__':
    main()

#Answer = 221616000        
