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
            line = next(get_line)
            a, d = [int(x) for x in re.findall(r'\d+', line)]
            line = next(get_line)
            b, e = [int(x) for x in re.findall(r'\d+', line)]
            line = next(get_line)
            c, f = [int(x)+10000000000000 for x in re.findall(r'\d+', line)]
        except StopIteration:
            break

        A = ((c * e) - (b * f)) / ((a * e) - (b * d))
        B = ((c * d) - (a * f)) / ((b * d) - (a * e))
        if A.is_integer() and B.is_integer():
            min_tokens += (3 * A) + B
    
    #Get the last entry. Need to clean this up.

    A = ((c * e) - (b * f)) / ((a * e) - (b * d))
    B = ((c * d) - (a * f)) / ((b * d) - (a * e))
    if A.is_integer() and B.is_integer():
        min_tokens += (3 * A) + B
            
    print(f'Min Tokens = {int(min_tokens)}')

if __name__ == '__main__':
    main()

#Answer = 107824497933339