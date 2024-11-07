from itertools import pairwise
from collections import Counter


DAY = '14'
LEVEL = 20


def perf_insert(poly, rules, lvl):
    for _ in range(lvl):
        new_poly = list()
        for poly_pair in pairwise(poly):
            new_poly.extend([poly_pair[0], rules[poly_pair]])
        new_poly.extend(poly_pair[1])
        poly=new_poly

    poly.pop(-1)
    return poly


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    polymer = input_data[0]

    rules = dict()

    for line in input_data[2:]:
        pair, insert = line.split(' -> ')
        rules[(pair[0], pair[1])] = insert

    poly_memory = dict()
    poly_counter = Counter()

    for poly_pair in pairwise(polymer):
        if poly_pair not in poly_memory:
            exp_poly = perf_insert(poly_pair, rules, LEVEL)
            poly_memory[poly_pair] = exp_poly
        else:
            exp_poly = poly_memory[poly_pair]

        poly_counter.update(exp_poly)

    poly_counter.update(poly_pair[1])

    max_ele = max(poly_counter.values())
    min_ele = min(poly_counter.values())

    print(f'Max - min: {max_ele - min_ele}')
    pass


if __name__ == '__main__':
    main()

#Answer = 2657
