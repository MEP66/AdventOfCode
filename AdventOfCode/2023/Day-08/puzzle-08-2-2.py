from collections import defaultdict
import re


def puzzle08():

    all_maps: dict(dict(str, str)) = defaultdict()

    filename = r'./Day-08/Input-08.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    directions: list(str) = [input_data[0]]
    path_maps: set(str) = set()

    for line in input_data[2:]:
        nodes = re.findall('[A-Z]+', line)
        all_maps[nodes[0]] = {'L' : nodes[1], 'R' : nodes[2]}
        if nodes[0].endswith('A'):
            path_maps.append(nodes[0])

    all_paths: dict(dict(str, str)) = defaultdict()
    max_nav: int = len(directions)

    for startnode in path_maps:
        steps: int = 0
        nav_pointer: int = 0
        currentnode = startnode
        currentpath = [startnode, 0]
        steps = 0
        while True:
            steps += 1
            currentnode = all_maps[currentnode][directions[nav_pointer]]
            if currentnode.endswith('Z'):
                currentpath.append(str(steps))
                print(steps)
            if currentnode == startnode:
                currentpath[1] = steps
                print(f'******** {steps}')
                break
            nav_pointer += 1
            if nav_pointer == max_nav:
                nav_pointer = 0
        all_paths.append(currentpath)

    pass
    
    print(f'{steps} total steps.')


if __name__ == '__main__':
    puzzle08()


# Answer: 