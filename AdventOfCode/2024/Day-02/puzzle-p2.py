from collections import Counter
from itertools import combinations

DAY = '02'


def pairwise(iterable):
    a = iter(iterable)
    b = iter(iterable)
    next(b)
    return [p for p in zip(a, b)]

def is_unsafe(numlist):
    dist_count = Counter([pair[1]-pair[0] for pair in pairwise(numlist)])
    sign_count = Counter([(x > 0) - (x < 0) for x in dist_count.keys()])

    unsafe = False
    if len(sign_count) != 1:
        unsafe = True
    else:
        if any([c not in [-3, -2, -1, 1, 2, 3] for c in dist_count]):
           unsafe = True
    return unsafe

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[int(x) for x in line.split(' ')] for line in f.read().splitlines()]

    unsafe = 0
    for line in input_data:
        if is_unsafe(line):
            for line_m1 in combinations(line, len(line)-1):
                if not is_unsafe(line_m1):
                    break
            else:
                unsafe += 1
    
    print(f'Number safe: {len(input_data)-unsafe}')


if __name__ == '__main__':
    main()

#Answer = 364