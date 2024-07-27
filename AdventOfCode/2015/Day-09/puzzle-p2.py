import re
import itertools

DAY = '09'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    nodes = set()
    dist_lookup = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            city1, city2, dist = re.split(' to | = ', line.strip())
            dist_lookup[(city1, city2)] = int(dist)
            dist_lookup[(city2, city1)] = int(dist)
            nodes.add(city1)
            nodes.add(city2)

    all_nodes = list(nodes)
    start_node = all_nodes.pop()

    all_perms = itertools.permutations(nodes)
    max_found = 0

    for entry in all_perms:
        all_segments = [(entry[i], entry[i+1]) for i in range(len(entry) - 1)]
        all_segments.insert(0, (start_node, all_nodes[0]))

        all_distances = [dist_lookup[s] for s in all_segments]
        this_distance = sum(all_distances) - min(all_distances)
        
        max_found = max(max_found, this_distance)

    print(max_found)

if __name__ == '__main__':
    main()

#Answer = 736
