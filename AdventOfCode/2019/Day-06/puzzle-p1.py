from collections import defaultdict


DAY = '06'


def calc_orbits(p, a):
    o_count = 0
    while a[p]['from'] != None:
        o_count += 1
        p = a[p]['from']
    return o_count


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [tuple(line.split(')')) for line in f.read().splitlines()]

    all_orbits = defaultdict(lambda: {'to' : list(), 'from' : None})

    for stationary, orbiting in input_data:
        all_orbits[stationary]['to'].append(orbiting)
        all_orbits[orbiting]['from'] = stationary
    
    total_orbits = 0

    for planet in all_orbits.keys():
        total_orbits += calc_orbits(planet, all_orbits)

    print(f'Total orbits = {total_orbits}')


if __name__ == '__main__':
    main()

#Answer = 162439