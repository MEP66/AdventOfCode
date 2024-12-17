from math import inf
from heapq import heapify, heappop, heappush
from collections import defaultdict

DAY = '16'

# Coordinates are in (x, y) or (c, r) format, with + down and right.
# The secret to this puzzle is to track weights, paths, etc, as (col, row, dir),
# and when you change direction, don't change cell location - just the direction.

moves = {'e': (1, 0), 's': (0, 1), 'w': (-1, 0), 'n': (0, -1)}

class Graph:
    def __init__(self, graph: list()):
        self._graph = graph
        self.max_x = len(self._graph[0])-1
        self.max_y = len(self._graph)-1
        self.previous_paths = defaultdict(list)

    def node_weight(self, nbrnode, curnode):
        # I shouldn't have to worry about 180 degree turns, since that would
        # result in a visited node, which would never be re-evaluated.
        if nbrnode[2] == curnode[2]:
            return 1
        else:
            return 1000

    def neighbors(self, node):
        nbr = list()
        c, r, d = node
        for step in moves:
            if self._graph[r+moves[step][1]][c+moves[step][0]] != '#':
                if step == d:
                    nbr.append((c+moves[step][0], r+moves[step][1], step))
                else:
                    # If changing direction, stay in the same cell. Change direction only.
                    nbr.append((c, r, step))
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

            for neighbor in self.neighbors(current_node):
                tentative_distance = current_distance + self.node_weight(neighbor, current_node)
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    self.previous_paths[neighbor] = [current_node]
                    heappush(pq, (tentative_distance, neighbor))
                elif tentative_distance == distances[(neighbor)]:
                    self.previous_paths[neighbor].append(current_node)

        return distances

def get_all_short_paths(node, paths, pathset):
    if node in paths:
        for newnode in paths[node]:
            pathset.add((node[0], node[1]))  # Here is where we strip out the direction information
            get_all_short_paths(newnode, paths, pathset)
    else:
        pathset.add((node[0], node[1]))  # Catch the start node, don't include direction information


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        maze = [[x for x in line] for line in f.read().splitlines()]

    for ri, row in enumerate(maze):
        for ci, t in enumerate(row):
            if t == 'S':
                startpos = (ci, ri, 'e')
            if t == 'E':
                endpos = (ci, ri)

    maze_graph = Graph(maze)

    distances = maze_graph.shortest_distances(startpos) # Solve the puzzle.

    paths = dict(maze_graph.previous_paths)  # Important to convert this from defaultdict to dict
    
    # Get endpoint coming from the direction with the smallest cost.

    shortest_path = min([distances[(endpos[0], endpos[1], d)] for d in ('n', 'e', 's', 'w')])
    for d in ('n', 'e', 's', 'w'):
        if distances[(endpos[0], endpos[1], d)] == shortest_path:
            shortest_end = (endpos[0], endpos[1], d)
            break
    
    pathset = set()
    get_all_short_paths(shortest_end, paths, pathset)
    print(f'Total number of tiles = {len(pathset)}')


if __name__ == '__main__':
    main()

#Answer = 527