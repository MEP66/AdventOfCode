import re
#import numpy as np


DAY = '13'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    get_line = iter(input_data)

    min_tokens = 0
    while True:
        try:
            line = next(get_line)
            x1, y1 = [int(x) for x in re.findall(r'\d+', line)]
            line = next(get_line)
            x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
            line = next(get_line)
            r1, r2 = [int(x)+10000000000000 for x in re.findall(r'\d+', line)]

            A = ((r1 * y2) - (x2 * r2)) / ((x1 * y2) - (x2 * y1))
            B = ((r1 * y1) - (x1 * r2)) / ((x2 * y1) - (x1 * y2))
            
            if A.is_integer() and B.is_integer():
                min_tokens += (3 * A) + B

            line = next(get_line)
        except StopIteration:
            break
            
    print(f'Min Tokens = {int(min_tokens)}')

if __name__ == '__main__':
    main()

#Answer = 107824497933339