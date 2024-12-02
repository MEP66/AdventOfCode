from collections import Counter
from itertools import combinations

DAY = '02'


def pairwise(iterable):
    a = iter(iterable)
    b = iter(iterable)
    next(b)
    return [p for p in zip(a, b)]

def is_safe(numlist):
    dist_count = Counter([pair[1]-pair[0] for pair in pairwise(numlist)])
    sign_count = Counter([(x > 0) - (x < 0) for x in dist_count])

    if len(sign_count) == 1 and all([c in [-3, -2, -1, 1, 2, 3] for c in dist_count]):
        return True
    return False


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[int(x) for x in line.split(' ')] for line in f.read().splitlines()]

    total_safe = 0
    for line in input_data:
        if is_safe(line):
            total_safe += 1
        else:
            for line_m1 in combinations(line, len(line)-1):
                if is_safe(line_m1):
                    total_safe += 1
                    break
    
    print(f'Number safe: {total_safe}')


if __name__ == '__main__':
    main()

#Answer = 364