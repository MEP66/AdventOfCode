
# https://www.codecademy.com/learn/learn-data-structures-and-algorithms-with-python/modules/trees/cheatsheet

from collections import namedtuple
import sys

DAY = '07'

FileValue = namedtuple('FileValue', 'size name')

class TreeNode:
    def __init__(self, name: str, parent = None):
        self.name = name
        self.value = [] # data
        self.size = 0
        self.parent = parent
        self.children = [] # references to other nodes

    def add_value(self, fileinfo: FileValue):
        # adds a value to a node.
        self.value.extend(fileinfo)
        self.update_size(fileinfo.size)

    def update_size(self, filesize: int):
        # updates the size of the directory, and up the tree
        self.size += filesize
        if self.parent != None:
            self.parent.update_size(filesize)
    
    def add_child(self, name: str):
        # creates parent-child relationship
        c_node = TreeNode(name, parent = self)
        self.children.append(c_node)

    def traverse_down(self, cname: str):
        # traverses down to a child node
        for childnode in self.children:
            if childnode.name == cname:
                return childnode
        print(f'Childnode {cname} does not exist.')
        sys.exit()
    
    def traverse_up(self):
        if self.parent == None:
            print('Cannot traverse up from root.')
            sys.exit()
        return self.parent

    def traverse_all(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        all_nodes = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            nodes_to_visit += current_node.children
            all_nodes += current_node.children
        return all_nodes

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    root = TreeNode('root')
    current_node = root
    proc_ls = False

    for line in input_data:
        if not proc_ls or (proc_ls and line[0] == '$'):
            proc_ls = False
            if line[0:4] == '$ cd':
                dir = line[5:]
                match dir:
                    case '/':
                        current_node = root
                    case '..':
                        current_node = current_node.traverse_up()
                    case _:
                        current_node = current_node.traverse_down(dir)
            elif line[0:4] == '$ ls':
                proc_ls = True
        else:
            if line[0].isdigit():
                size, name = line.split(' ')
                current_node.add_value(FileValue(int(size), name))
            else:
                dir = line.split(' ')[1]
                current_node.add_child(dir)

    MAXDIRSIZE = 100000
    sum = 0
    for node in root.traverse_all():
        if node.size <= MAXDIRSIZE:
            sum += node.size
    print(f'The sum of directories < 100K is: {sum}')

if __name__ == '__main__':
    main()

# Answer = 1501149