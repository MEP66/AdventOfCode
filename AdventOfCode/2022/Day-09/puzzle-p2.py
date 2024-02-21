# Day 09

from collections import namedtuple

DAY = '09'

Coord = namedtuple('Coord', ['x', 'y'])


moves = {'U': Coord(x=0, y=1), 'D': Coord(x=0, y=-1), 'R': Coord(x=1, y=0), 'L': Coord(x=-1, y=0)}


class Node:
    def __init__(self, parent = None):
        self.coord = Coord(x=0, y=0) # data
        self.track = set(self.coord)
        self.parent = parent
        self.child = None # references to child node

    def track_visited(self):
        # adds a value to a node.
        self.track.add(self.coord)
    
    def add_child(self):
        # creates and return a child node
        c_node = Node(parent = self)
        self.child = c_node
        return c_node

    def move_headnode(self, dir):
        self.coord = Coord(self.coord.x + moves[dir].x, self.coord.y + moves[dir].y)
        self.child.move_node()
    
    def move_node(self):
        absdist = Coord(abs(self.parent.coord.x - self.coord.x), abs(self.parent.coord.y - self.coord.y))

        if not ((absdist.x == 0 or absdist.x == 1) and (absdist.y == 0 or absdist.y == 1)):
            if absdist.x == 2:
                newx = int((self.coord.x + self.parent.coord.x)/2)
            if absdist.y == 2:
                newy = int((self.coord.y + self.parent.coord.y)/2)
            if absdist.x == 1:
                newx = self.parent.coord.x
            if absdist.y == 1:
                newy = self.parent.coord.y
            if absdist.x == 0:
                newx = self.coord.x
            if absdist.y == 0:
                newy = self.coord.y
            self.coord = Coord(x=newx, y=newy)

            if self.child != None:
                self.child.move_node()
            else:
                self.track_visited()

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    headknot = Node()
    currentknot = headknot
    for x in range(9):
        currentknot = currentknot.add_child()
    tailknot = currentknot

    for line in input_data:
        command = line.split(' ')
        movdir = command[0]
        movdist = int(command[1])

        for _ in range(movdist):
            headknot.move_headnode(movdir)

    print(f'The total number of tail visits is: {len(tailknot.track)}')


if __name__ == '__main__':
    main()

# Answer = 2259