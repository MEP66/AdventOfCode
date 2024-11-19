from math import inf
from heapq import heapify, heappop, heappush


DAY = '13'

START = (1, 1)
#FAVORITE = 10
#DESTINATION = (7, 4)
FAVORITE = 1352
DESTINATION = (31, 39)


def get_space(coord):
    x = coord[0]
    y = coord[1]
    temp = bin((x*x + 3*x + 2*x*y + y + y*y) + FAVORITE)[2:]
    calc = sum([int(x) for x in list(temp)])
    if not(calc % 2):
        return 1
    return inf


class Graph:
    def __init__(self, graph: list()):
        self._graph = graph
        self.max_x = len(self._graph[0])-1
        self.max_y = len(self._graph)-1

    def node_weight(self, node):
        #This is row/col, so I have to flip from x,y coord.
        return self._graph[node[1]][node[0]]

    def neighbors(self, node):
        nbr = list()
        if node[0] != 0:
            nbr.append((node[0]-1, node[1]))
        if node[0] != self.max_x:
            nbr.append((node[0]+1, node[1]))
        if node[1] != 0:
            nbr.append((node[0], node[1]-1))
        if node[1] != self.max_y:
            nbr.append((node[0], node[1]+1))
        return nbr

    def shortest_distances(self, source):
        distances = {(x, y):inf for x in range(self.max_x+1) for y in range(self.max_y+1)}
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
    max_x = DESTINATION[0] + 10
    max_y = DESTINATION[1] + 10

    maze_in = list()
    for y in range(max_y):
        row = list()
        for x in range(max_x):
            row.append(get_space((x, y)))
        maze_in.append(row)

    maze_graph = Graph(maze_in)

    distances = maze_graph.shortest_distances(START)
    
    print(f'Min distance from {START} to {DESTINATION} is {distances[DESTINATION]}')

if __name__ == '__main__':
    main()

#Answer = 90