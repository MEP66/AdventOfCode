from dataclasses import dataclass
from collections import defaultdict
import re


@dataclass
class Map:
    L: str
    R: str


def puzzle08():

    all_maps: dict(str, Map) = defaultdict()
    BEGIN = 'AAA'
    END = 'ZZZ'

    filename = r'./Day-08/Input-08.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    directions: list(str) = list(input_data[0])

    for line in input_data[2:]:
        nodes = re.findall('[A-Z]+', line)
        all_maps[nodes[0]] = (Map(nodes[1], nodes[2]))

    steps: int = 0
    nav_pointer: int = 0
    max_nav: int = len(directions)
    current_node: str = BEGIN
    while current_node != END:
        steps +=1
        current_node = getattr(all_maps[current_node], directions[nav_pointer])
        nav_pointer += 1
        if nav_pointer == max_nav:
            nav_pointer = 0
    
    print(steps)


if __name__ == '__main__':
    puzzle08()


# Answer: 16531Day-08