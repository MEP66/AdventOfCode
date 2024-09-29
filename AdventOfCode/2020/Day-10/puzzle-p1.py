from collections import Counter
from itertools import tee


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
    diff_counter = Counter([y-x for x, y in pairwise(input_data)])
    print(f'Answer = {diff_counter[1] * diff_counter[3]}')


if __name__ == '__main__':
    main()

#Answer 1998