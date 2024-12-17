from math import inf
from heapq import heapify, heappop, heappush


DAY = '16'

# Coordinates are in (x, y) or (c, r) format, with + down and right.

moves = {'e': (1, 0), 's': (0, 1), 'w': (-1, 0), 'n': (0, -1)}

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
        c, r, _ = node
        for step in moves:
            if self._graph[r+moves[step][1]][c+moves[step][0]] != '#':
                nbr.append((c+moves[step][0], r+moves[step][1], step))
        return nbr

    def shortest_distances(self, source):
        distances = {(x, y):inf for x in range(self.max_x+1) for y in range(self.max_y+1)}
        distances[(source[0], source[1])] = 0

        pq = [(0, source)]
        heapify(pq)

        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if (current_node[0], current_node[1]) in visited:
                continue
            visited.add((current_node[0], current_node[1]))

            for neighbor in self.neighbors(current_node):
                tentative_distance = current_distance + self.node_weight(neighbor, current_node)
                if tentative_distance < distances[(neighbor[0], neighbor[1])]:
                    distances[(neighbor[0], neighbor[1])] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
        
        return distances
    

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        maze = [[x for x in line] for line in f.read().splitlines()]

    for ri, row in enumerate(maze):
        for ci, t in enumerate(row):
            if t == 'S':
                startpos = (ci, ri, 'e')
                #maze[ri][ci] = '.'
            if t == 'E':
                endpos = (ci, ri)
                #maze[ri][ci] = '.'

    maze_graph = Graph(maze)

    distances = maze_graph.shortest_distances(startpos)
    
    print(f'Shortest distance = {distances[(endpos[0], endpos[1])]}')


if __name__ == '__main__':
    main()

#Answer = 102460