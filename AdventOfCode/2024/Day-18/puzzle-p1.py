from math import inf
from heapq import heapify, heappop, heappush
from collections import defaultdict, namedtuple



DAY = '18'

MAXROW = 6
MAXCOL = 6
MAXMEM = 12
MAXROW = 70
MAXCOL = 70
MAXMEM = 1024


# Coordinates are in (x, y) or (c, r) format, with + down and right.

moves = {'e': (1, 0), 's': (0, 1), 'w': (-1, 0), 'n': (0, -1)}

Coord = namedtuple('Coord', ['c', 'r'])


class Graph:
    def __init__(self, graph: list()):
        self._graph = graph
        self.max_x = len(self._graph[0])-1
        self.max_y = len(self._graph)-1

    def node_weight(self, nbrnode, curnode):
        # I shouldn't have to worry about 180 degree turns, since that would
        # result in a visited node, which would never be re-evaluated.
        if nbrnode[2] == curnode[2]:
            return 1
        else:
            return 1001

    def neighbors(self, node):
        nbr = list()
        for step in moves:
            nc = node.c + moves[step][0]
            nr = node.r + moves[step][1]
            if 0 <= nc <= MAXCOL and 0 <= nr <= MAXROW:
                if self._graph[nr][nc] != '#':
                    nbr.append(Coord(c=nc, r=nr))
        return nbr

    def shortest_distances(self, source):
        distances = defaultdict(lambda: inf)
        distances[source] = 0

        pq = [(0, source)]
        heapify(pq)

        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if (current_node) in visited:
                continue
            visited.add((current_node))

            for neighbor in self.neighbors(current_node):
                tentative_distance = current_distance + 1
                if tentative_distance < distances[(neighbor)]:
                    distances[(neighbor)] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
        
        return distances
    

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[int(x) for x in line.split(',')] for line in f.read().splitlines()]

    memmap = [['.' for col in range(MAXCOL+1)] for line in range(MAXROW+1)]
    for mp in input_data[:MAXMEM]:
        memmap[mp[1]][mp[0]] = '#'

    mem_graph = Graph(memmap)
    start = Coord(c=0, r=0)
    end = Coord(c=MAXCOL, r=MAXROW)

    distances = mem_graph.shortest_distances(start)
    
    print(f'Shortest distance = {distances[end]}')

if __name__ == '__main__':
    main()

#Answer = 438