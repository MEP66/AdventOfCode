from math import inf
from heapq import heapify, heappop, heappush
from collections import defaultdict, namedtuple

DAY = '20'

CHEAT_THRESHOLD = 100
MAX_CHEAT = 20

# Coordinates are in (x, y) or (c, r) format, with + down and right.

Coord = namedtuple('Coord', ['c', 'r'])

moves = {'e': Coord(c=1, r=0), 's': Coord(c=0, r=1), 
         'w': Coord(c=-1, r=0), 'n': Coord(c=0, r=-1)}

def shortcut(sp, ep, endpos, mhtdist, distances):
    return distances[sp] + mhtdist + (distances[endpos] - distances[ep])

def manhattan_dist(sp, ep):
    return (abs(sp[0]-ep[0]) + abs(sp[1]-ep[1]))

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
                    self.previous_paths[neighbor] = current_node
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
    orig_dist = distances[endpos]
    paths = list(maze_graph.previous_paths.values())
    paths.append(endpos)
    
    # Find manhattan distance from every point on the path to every other point.
    # If distance <= MAX_CHEAT and savings >= CHEAT_THREASHOLD, count it.

    total_cheats = 0

    for si, sp in enumerate(paths):
        for ei, ep in enumerate(paths[si+2:], si+2):
            mhtdist = manhattan_dist(sp, ep)
            if mhtdist <= MAX_CHEAT:
                if orig_dist - shortcut(sp, ep, endpos, mhtdist, distances) >= CHEAT_THRESHOLD:
                    total_cheats += 1
    
    print(f'Total cheats >= to {CHEAT_THRESHOLD} = {total_cheats}')


if __name__ == '__main__':
    main()

#Answer = 983054