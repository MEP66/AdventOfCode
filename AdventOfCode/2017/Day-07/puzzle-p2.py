import re
from collections import Counter

DAY = '07'


def create_node(t, nam, wght = None, frm = None, to = None):
    if nam in t:
        if wght:
            t[nam]['weight'] = wght
            t[nam]['total'] = wght
        if frm:
            t[nam]['fromlink'] = frm
        if to:
            t[nam]['tolink'] = to
    else:
        t[nam] = {'weight': wght, 'fromlink': frm, 'tolink': to, 'total': wght}

    if to:
        for entry in to:
            create_node(t, entry, frm = nam)

def gettotalweight(tree, node):
    if tree[node]['tolink'] is None:
        return tree[node]['weight']
    else:
        tree[node]['total'] = sum([gettotalweight(tree, n) for n in tree[node]['tolink']]) + tree[node]['weight']
        return tree[node]['total']


def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    tree = dict()
    
    for line in input_data:
        x = re.search(r'(.*) \((\d*)\)', line)
        name = x.group(1)
        weight = int(x.group(2))

        if line.find(' -> ') != -1:
            x = line.split(' -> ')
            tolink = tuple(x[1].split(', '))
            create_node(tree, name, wght= weight, to = tolink)
        else:
            create_node(tree, name, wght = weight)

    for k, v in tree.items():
        if v['fromlink'] is None:
            root = k
            break

    gettotalweight(tree, root)

    # Ugh, this is ugly. There has to be a better way.

    currentnode = root
    while tree[currentnode]['tolink'] is not None:
        nodetotals = list()
        for nnode in tree[currentnode]['tolink']:
            nodetotals.append((nnode, tree[nnode]['total']))
        for nodeweight in nodetotals:
            print(nodeweight)
        print()
        weights = [w[1] for w in nodetotals]

        counts = Counter(weights)

        try:
            oddball = (list(counts.keys())[list(counts.values()).index(1)])
        except ValueError:
            pass

        else:
            for node in nodetotals:
                if node[1] == oddball:
                    currentnode = node[0]
                    break
    pass

if __name__ == '__main__':
    main()

#Answer = 1505  (1579 - 33 - 33 - 8)