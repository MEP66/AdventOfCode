import re


DAY = '07'


def create_node(t, nam, wght = None, frm = None, to = None):
    if nam in t:
        if wght:
            t[nam]['number'] = wght
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

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
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
    
    for k, v in tree.items():
        if v['tolink'] is None:
            totalweight = v['weight']
            while v['fromlink'] is not None:
                backnode = v['fromlink']
                totalweight += tree[backnode]['total']
                tree[backnode]['total'] = totalweight
                v = tree[backnode]

    pass


if __name__ == '__main__':
    main()

#Answer = hlhomy