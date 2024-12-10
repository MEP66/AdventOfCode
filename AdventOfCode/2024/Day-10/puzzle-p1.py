

DAY = '10'


dir = ((0, -1), (1, 0), (0, 1), (-1, 0))

def neighbors(c, tmap):
    all_neighbors = []
    c, r = c
    for d in dir:
        nc = c + d[0]
        nr = r + d[1]
        if (0 <= nc < len(tmap[0])) and (0 <= nr < len(tmap)):
            all_neighbors.append((nc, nr))
    return all_neighbors

def all_nines_found(coord, lvl, tmap):
    valid_paths = list()
    nines_found = set()
    for ncoord in neighbors(coord, tmap):
        if tmap[ncoord[1]][ncoord[0]] == lvl:
            valid_paths.append(ncoord)
    if lvl == 9:
        return set(valid_paths)
    else:
        lvl += 1
        for c in valid_paths:
            nines_found = nines_found.union(all_nines_found(c, lvl, tmap))
        return nines_found
                

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        topo_map = [[int(x) for x in line] for line in f.read().splitlines()]

    sum_scores = 0
    for ri, row in enumerate(topo_map):
        for ci, n in enumerate(row):
            if n == 0:
                sum_scores += len(all_nines_found((ci, ri), 1, topo_map))
                pass

    print(f'Sum of path scores = {sum_scores}')

if __name__ == '__main__':
    main()

#Answer = 733