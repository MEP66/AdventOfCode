
from math import inf
from heapq import heapify, heappop, heappush


# Got a little assistance from these:
# https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php
# https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python


DAY = '15'


class Graph:
    def __init__(self, graph: list()):
        self._graph = graph
        self.maxrow = len(self._graph)-1
        self.maxcol = len(self._graph[0])-1
    
    def node_weight(self, node):
        return self._graph[node[0]][node[1]]
    
    def neighbors(self, node):
        nbr = list()
        if node[0] != 0:
            nbr.append((node[0]-1, node[1]))
        if node[0] != self.maxrow:
            nbr.append((node[0]+1, node[1]))
        if node[1] != 0:
            nbr.append((node[0], node[1]-1))
        if node[1] != self.maxcol:
            nbr.append((node[0], node[1]+1))
        return nbr

    def shortest_distances(self, source):
        distances = {(r, c):inf for r in range(self.maxrow+1) for c in range(self.maxcol+1)}
        distances[source] = 0

        pq = [(0, source)]
        heapify(pq)

        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor in self.neighbors(current_node):
                tentative_distance = current_distance + self.node_weight(neighbor)
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
        
        return distances


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        tile = [[int(x) for x in line] for line in f.read().splitlines()]
        numcols = len(tile[0])
        for tile_ext in range(4):
            for ri, row in enumerate(tile):
                for ci in range(numcols):
                    tile[ri].append(row[ci]+tile_ext+1 if row[ci]+tile_ext+1<10 else row[ci]+tile_ext-8)
        numrows = len(tile)
        numcols = len(tile[0])
        for tile_ext in range(4):
            for ri in range(numrows):
                newrow = list()
                for ci in range(numcols):
                    newrow.append((tile[ri][ci]+tile_ext+1) if (tile[ri][ci]+tile_ext+1)<10 else tile[ri][ci]+tile_ext-8)
                tile.append(newrow)
        
        risk_map = Graph(tile)
        del tile

    distances = risk_map.shortest_distances((0, 0))

    print(distances[(risk_map.maxrow, risk_map.maxcol)])


if __name__ == '__main__':
    main()

#Answer = 2904