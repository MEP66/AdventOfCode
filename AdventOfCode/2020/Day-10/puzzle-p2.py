from collections import Counter
from itertools import tee, groupby


DAY = '10'


def pairwise(iterable):
    a , b = tee(iterable)
    next(b, None)
    return zip(a, b)

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().splitlines()]
    
    input_data.append(0)
    input_data.append(max(input_data) + 3)
    input_data.sort()
    diffs = [y-x for x, y in pairwise(input_data)]
    groups = [(k, len(list(g))) for k, g in groupby(diffs)]
    
    num_paths = 1
    for k, c in groups:
        if k == 1:
            match c:
                case 1:
                    mult = 1
                case 2:
                    mult = 2
                case 3:
                    mult = 4
                case _:
                    mult = (c - 3) * 7
            num_paths *= mult
    

    print(f'Answer = {num_paths}')


if __name__ == '__main__':
    main()

#Answer 347250213298688