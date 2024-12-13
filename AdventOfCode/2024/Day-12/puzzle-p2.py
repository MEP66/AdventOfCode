from collections import defaultdict


DAY = '12'

# Coordinates are in (x, y) or (c, r) format with + down and right.

moves = {'top': (0, -1), 'right': (1, 0), 'bottom': (0, 1), 'left': (-1, 0)}


def segments(nums):

    # Found help with this one:
    # https://stackoverflow.com/questions/2361945/detecting-consecutive-integers-in-a-list

    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    return len(gaps) + 1


def get_neighbors_and_edges(coord, gmap, edges):
    c = coord[0]
    r = coord[1]
    nbrs = set()
    for e, m in moves.items():
        nc = c + m[0]
        nr = r + m[1]
        if ((0 <= nc < len(gmap[0]) and 0 <= nr < len(gmap)) and
                gmap[nr][nc] == gmap[r][c]):
            nbrs.add((nc, nr))
        else:
            match e:
                case 'top'|'bottom':
                    edges[e][r].append(c)
                case 'right'|'left':
                    edges[e][c].append(r)
    return (nbrs, edges)


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
        edges = {'top': defaultdict(list), 'bottom': defaultdict(list), 'left': defaultdict(list), 'right': defaultdict(list)}

        neighbors, edges = get_neighbors_and_edges(cplot, garden_map, edges)
        #perimeter = 4 - len(neighbors)
        nbrs_not_visited = neighbors.copy()
        while nbrs_not_visited:
            nbrs_visited.add(cplot := nbrs_not_visited.pop())
            area += 1
            all_not_visited.remove(cplot)

            neighbors, edges = get_neighbors_and_edges(cplot, garden_map, edges)
            #perimeter += (4 - len(neighbors))
            nbrs_not_visited = nbrs_not_visited.union((set(neighbors) - nbrs_visited))
        
        # Determine number of sides

        s = 0
        for edge in edges.values():
            for r_or_c in edge.values():
                s += segments(r_or_c)

        total_cost += s * area

    print(f'Total cost = {total_cost}')


if __name__ == '__main__':
    main()

#Answer = 834828