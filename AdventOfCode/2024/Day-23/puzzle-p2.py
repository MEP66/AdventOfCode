from itertools import combinations


# https://stackoverflow.com/questions/1705824/finding-cycle-of-3-nodes-or-triangles-in-a-graph/43108568#43108568
# https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length


DAY = '23'

def generate_combo(iterable):
    for i in range(2, len(iterable)+1):
        for combo in combinations(iterable, i):
            yield combo

def generate_meshes(nodes):
    for v in nodes.values():
        connected_nodes = [nodes[x] for x in v]

        max_mesh = set()
        for c in generate_combo(connected_nodes):
            mesh = set.intersection(*c)
            if len(mesh) == len(c) and len(mesh) > len(max_mesh):
                max_mesh = mesh
        max_mesh = list(max_mesh)
        yield max_mesh

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [{line[:2], line[3:]} for line in f.read().splitlines()]

    all_networks = dict()
    for a, b in input_data:
        if a not in all_networks:
            all_networks[a] = {a, b}
        else:
            all_networks[a].add(b)
        if b not in all_networks:
            all_networks[b] = {b, a}
        else:
            all_networks[b].add(a)
    
    meshes = list(generate_meshes(all_networks))

    largest_mesh = list()
    for m in meshes:
        if len(m) > len(largest_mesh):
            largest_mesh = m
    largest_mesh.sort()
    
    print(f'The largest mesh is: {largest_mesh}')
    print(f'The password is {','.join(largest_mesh)}')

if __name__ == '__main__':
    main()

#Answer = ac,ed,fh,kd,lf,mb,om,pe,qt,uo,uy,vr,wg