

DAY = '12'

# Coordinates are in (x, y) or (c, r) format with + down and right.

moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_neighbors(coord, gmap):
    c = coord[0]
    r = coord[1]
    nbrs = set()
    for m in moves:
        nc = c + m[0]
        nr = r + m[1]
        if ((0 <= nc < len(gmap[0]) and 0 <= nr < len(gmap)) and
                gmap[nr][nc] == gmap[r][c]):
            nbrs.add((nc, nr))
    return nbrs


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        garden_map = [[x for x in line] for line in f.read().splitlines()]

    all_not_visited = list()
    for ri, row in enumerate(garden_map):
        for ci, _ in enumerate(row):
            all_not_visited.append((ci, ri))

    total_cost = 0
    while all_not_visited:
        nbrs_visited = {cplot := all_not_visited.pop(0)}
        area = 1

        neighbors = get_neighbors(cplot, garden_map)
        perimeter = 4 - len(neighbors)
        nbrs_not_visited = neighbors.copy()
        while nbrs_not_visited:
            nbrs_visited.add(cplot := nbrs_not_visited.pop())
            area += 1
            all_not_visited.remove(cplot)

            neighbors = get_neighbors(cplot, garden_map)
            perimeter += (4 - len(neighbors))
            nbrs_not_visited = nbrs_not_visited.union((set(neighbors) - nbrs_visited))
        
        total_cost += perimeter * area

    print(f'Total cost = {total_cost}')

if __name__ == '__main__':
    main()

#Answer = 1381056