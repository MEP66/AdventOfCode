
# https://stackoverflow.com/questions/1705824/finding-cycle-of-3-nodes-or-triangles-in-a-graph/43108568#43108568

DAY = '23'


def generate_3node_rings(nodes):
    visited = set()
    for node_a in nodes:
        temp_visited = set()
        for node_b in nodes[node_a]:
            if node_b in visited:
                continue
            for node_c in nodes[node_b]:
                if node_c in visited:
                    continue
                if node_c in temp_visited:
                    continue
                if node_a in nodes[node_c]:
                    yield(node_a, node_b, node_c)
            temp_visited.add(node_b)
        visited.add(node_a)

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [{line[:2], line[3:]} for line in f.read().splitlines()]

    all_networks = dict()
    for a, b in input_data:
        if a not in all_networks:
            all_networks[a] = {b}
        else:
            all_networks[a].add(b)
        if b not in all_networks:
            all_networks[b] = {a}
        else:
            all_networks[b].add(a)
    
    rings = list(generate_3node_rings(all_networks))
    
    trings = 0
    for ring in rings:
        for node in ring:
            if node[0] == 't':
                trings += 1
                break
    
    
    print(f'Total number of "t" triangle nodes: {trings}')

if __name__ == '__main__':
    main()

#Answer = 1512