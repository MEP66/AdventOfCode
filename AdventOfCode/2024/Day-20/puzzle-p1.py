from math import inf
from heapq import heapify, heappop, heappush
from collections import defaultdict, namedtuple

DAY = '20'

CHEAT_THRESHOLD = 100

# Coordinates are in (x, y) or (c, r) format, with + down and right.

Coord = namedtuple('Coord', ['c', 'r'])

moves = {'e': Coord(c=1, r=0), 's': Coord(c=0, r=1), 
         'w': Coord(c=-1, r=0), 'n': Coord(c=0, r=-1)}

class Graph:
    def __init__(self, graph: list()):
        self._graph = graph
        self.max_x = len(self._graph[0])-1
        self.max_y = len(self._graph)-1
        self.previous_paths = defaultdict(list)


    def neighbors(self, node):
        nbr = dict()
        for d, step in moves.items():
            try:
                if self._graph[nr := node.r+step.r][nc := node.c+step.c] != '#':
                    nbr[d] = Coord(nc, nr)
            except IndexError:
                pass
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
            visited.add(current_node)

            for neighbor in self.neighbors(current_node).values():
                tentative_distance = current_distance + 1
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    self.previous_paths[neighbor] = [current_node]
                    heappush(pq, (tentative_distance, neighbor))
                elif tentative_distance == distances[(neighbor)]:
                    self.previous_paths[neighbor].append(current_node)
        return distances


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        maze = [[x for x in line] for line in f.read().splitlines()]

    for ri, row in enumerate(maze):
        for ci, t in enumerate(row):
            if t == 'S':
                startpos = Coord(c=ci, r=ri)
            if t == 'E':
                endpos = Coord(c=ci, r=ri)

    maze_graph = Graph(maze)

    distances = maze_graph.shortest_distances(startpos) # Solve the puzzle.
    paths = dict(maze_graph.previous_paths)  # Important to convert this from defaultdict to dict
    
    # Find all walls with a path on two sides.

    total_cheats = 0
    for ri, row in enumerate(maze):
        for ci, t in enumerate(row):
            if t == '#':
                neighbors = maze_graph.neighbors(Coord(ci, ri))
                if (('n' in neighbors and 's' in neighbors) or
                    ('e' in neighbors and 'w' in neighbors)):
                    if ('n' in neighbors and 's' in neighbors):
                        nbr1 = (neighbors['n'], distances[neighbors['n']])
                        nbr2 = (neighbors['s'], distances[neighbors['s']])
                    else:
                        nbr1 = (neighbors['e'], distances[neighbors['e']])
                        nbr2 = (neighbors['w'], distances[neighbors['w']])
                    if abs(nbr1[1]-nbr2[1])-2 >= CHEAT_THRESHOLD:
                        total_cheats += 1
                
            
    

    print(f'Total cheats equal to {CHEAT_THRESHOLD} = {total_cheats}')


if __name__ == '__main__':
    main()

#Answer = 1375