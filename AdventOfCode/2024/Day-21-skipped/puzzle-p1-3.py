from collections import defaultdict, namedtuple
from math import inf
from heapq import heapify, heappop, heappush


DAY = '21'


#Coordinates are in (x, y) or (c, r) format with + down and right.

Coord = namedtuple('Coord', ['c', 'r'])
moves = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}


class Graph:
    def __init__(self, graph: list()):
        self._graph = graph
        self.max_x = len(self._graph[0])-1
        self.max_y = len(self._graph)-1
        self.previous_paths = defaultdict(list)

    def node_weight(self, nbrnode, curnode):
        # Since I have to do shortest path, I'm thinking I need to minimize
        # turns, so add an extra weight to those. 
        if nbrnode[1] == curnode[1]:
            return 1
        else:
            return 10

    def neighbors(self, node):
        nbr = list()
        c = node[0].c
        r = node[0].r
        d = node[1]
        for step in moves:
            if self._graph[r+moves[step][1]][c+moves[step][0]] != '#':
                nbr.append((Coord(c+moves[step][0], r+moves[step][1]), step))

                #if step == d:
                #    nbr.append((Coord(c+moves[step][0], r+moves[step][1]), step))
                #else:
                #    # If changing direction, stay in the same cell. Change direction only.
                #    nbr.append((Coord(c, r), step))
        return nbr

    def shortest_distances(self, src_coord):
        distances = defaultdict(lambda: inf)
        distances[src_coord[0]] = 0

        pq = [(0, src_coord)]
        self.previous_paths[src_coord[0]] = (Coord(-1, -1), '.')

        heapify(pq)

        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if (current_node[0]) in visited:
                continue
            visited.add(current_node[0])

            for neighbor in self.neighbors(current_node):
                tentative_distance = current_distance + self.node_weight(neighbor, current_node)
                if tentative_distance < distances[neighbor[0]]:
                    distances[neighbor[0]] = tentative_distance
                    self.previous_paths[neighbor[0]] = (current_node[0], self.previous_paths[current_node[0]][1]+neighbor[1])
                    heappush(pq, (tentative_distance, neighbor))
                #elif tentative_distance == distances[(neighbor)]:
                    #self.previous_paths[neighbor].append(current_node)
        return distances

    def get_keyseq(self, node): # (paths, pathset):
        if node:
            if node in self.previous_paths:
                keyseq = self.previous_paths[node][1] + self.get_keyseq(self.previous_paths[node][0])
                return keyseq
        return ''


class Robot:
    def __init__(self, keys):
        # Surround the graph in walls ('#'), to make boundary checking a bit easier.

        self._key_matrix = list()
        self._key_matrix.append(list('#' * (len(list(keys[0]))+2)))
        for line in keys:
            self._key_matrix.append(list('#' + line + '#'))
        self._key_matrix.append(list('#' * (len(list(keys[0]))+2)))
        
        self._key_graph = Graph(self._key_matrix)

        # Create a dictionary of Key coordinates and initialize start position to the 'A' key.
        self._key_coords = dict()
        for ri, row in enumerate(self._key_matrix):
            for ci, k in enumerate(row):
                if k != '#':
                    self._key_coords[k] = Coord(ci, ri)
        self._cur_key_ptr = (self._key_coords['A'], '.')

    def reset(self):
        self._cur_key_ptr = (self._key_coords['A'], '.')
    
    def press(self, dkey):
        distances = self._key_graph.shortest_distances(self._cur_key_ptr)
        #min_dist = inf
        #for c, v in distances.items():
        #    if c[0] == self._key_coords[dkey]:
        #        if v < min_dist:
        #            min_dist = v
        #            min_coord = c
        
        path = self._key_graph.get_keyseq(self._key_coords[dkey]) + 'A'

        self._cur_key_ptr = (self._key_coords[dkey], '.') 
        
        return path           #distances[self._key_coords[dkey]]


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        keycodes = [line for line in f.read().splitlines()]
    
    # Use '#' to represent invalid location.
    num_keypad = (('789'), ('456'), ('123'), ('#0A'))
    DoorRobot = Robot(num_keypad)

    dir_keypad = (('#^A'), ('<v>'))
    CntlRobot = Robot(dir_keypad)
    MeRobot = Robot(dir_keypad)

    result = 0

    for sequence in keycodes:
        DoorRobot.reset()
        CntlRobot.reset()
        MeRobot.reset()
        final_keysequence = list()
        
        for key in sequence:
            movements1 = DoorRobot.press(key)
            #for key1 in movements1:
                #movements2 = CntlRobot.press(key1)
                #for key2 in movements2:
                    #movements3 = MeRobot.press(key2)
                #final_keysequence += movements3
        result += (len(final_keysequence) * int(sequence[:3]))
    
    print(f'Final result = {result}')
    pass

if __name__ == '__main__':
    main()
