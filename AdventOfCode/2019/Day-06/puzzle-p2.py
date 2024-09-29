from collections import defaultdict


DAY = '06'


def get_orbit(p, a):
    orbit = list()
    while p != 'COM':
        p = a[p]['from']
        orbit.append(p)
    return orbit


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [tuple(line.split(')')) for line in f.read().splitlines()]

    all_orbits = defaultdict(lambda: {'to' : list(), 'from' : None})

    for stationary, orbiting in input_data:
        all_orbits[stationary]['to'].append(orbiting)
        all_orbits[orbiting]['from'] = stationary
    
    you_orbit = get_orbit('YOU', all_orbits)
    san_orbit = get_orbit('SAN', all_orbits)
    
    for planet in you_orbit:
        if planet in san_orbit:
            you_index = you_orbit.index(planet)
            san_index = san_orbit.index(planet)
            break

    print(f'Min transfers = {you_index + san_index}')


if __name__ == '__main__':
    main()

#Answer = 367