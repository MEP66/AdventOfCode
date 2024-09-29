from math import inf
from collections import Counter


DAY = '08'

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    WIDTH = 25
    HEIGHT = 6

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read()]

    rows = [input_data[r:r+WIDTH] for r in range(0, len(input_data), WIDTH)]
    images = [rows[c:c+HEIGHT] for c in range(0, len(rows), HEIGHT)]
    
    del rows, input_data
    
    fewest_zero = inf

    for image in images:
        counts = Counter([x for row in image for x in row])
        if counts[0] < fewest_zero:
            fewest_zero = counts[0]
            one_count = counts[1]
            two_count = counts[2]
    
    print(f'Result: {one_count * two_count}')


if __name__ == '__main__':
    main()

#Answer = 1690