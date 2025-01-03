import sys
import re
from dataclasses import dataclass
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

DAY = '09'

@dataclass
class Inp:
    city1: str
    city2: str
    dist: int

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
       
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
       
        graph.update(init_graph)
       
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                   
        return graph
   
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
   
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
   
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0 

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
   
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)
   
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    input_data = []
    nodes = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            c1, c2, d = re.split(' to | = ', line.strip())
            input_data.append(Inp(city1 = c1, city2 = c2, dist = int(d)))
            nodes.add(c1)
            nodes.add(c2)

    city_ref = dict()
    for offset, city in enumerate(nodes):
        city_ref[city] = offset

    data = {}
    data["distance_matrix"] = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for input in input_data:
        data["distance_matrix"][city_ref[input.city1]][city_ref[input.city2]] = input.dist
        data["distance_matrix"][city_ref[input.city2]][city_ref[input.city1]] = input.dist

    pass

if __name__ == '__main__':
    main()
