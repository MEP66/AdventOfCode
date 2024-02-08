from dataclasses import dataclass
from collections import defaultdict
import re


# @dataclass
# class Map:
#     L: str
#     R: str


def puzzle08():

    all_maps: dict(str, Map) = defaultdict()

    filename = r'./Day-08/Input-08.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    directions: list(int) = [0 if x == 'L' else 1 for x in list(input_data[0])]

    for line in input_data[2:]:
        nodes = re.findall('[A-Z0-9]+', line)
        all_maps[nodes[0]] = (nodes[1], nodes[2])

    path_maps = [node for node in all_maps.keys() if node.endswith('A')]

    steps: int = 0
    nav_pointer: int = 0
    max_nav: int = len(directions)
    
    print(path_maps)
    while not all([b.endswith('Z') for b in path_maps]):
        steps +=1
        path_maps = [all_maps[map][directions[nav_pointer]] for map in path_maps]
        nav_pointer += 1
        if nav_pointer == max_nav:
            nav_pointer = 0
    
    print(f'{steps} total steps.')


if __name__ == '__main__':
    puzzle08()


# Answer: 