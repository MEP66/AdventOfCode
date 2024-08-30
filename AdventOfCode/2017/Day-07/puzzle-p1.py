import re


DAY = '07'


def create_node(t, nam, num = None, frm = None, to = None):
    if nam in t:
        if num:
            t[nam]['number'] = num
        if frm:
            t[nam]['fromlink'] = frm
        if to:
            t[nam]['tolink'] = to
    else:
        t[nam] = {'number': num, 'fromlink': frm, 'tolink': to}

    if to:
        for entry in to:
            create_node(t, entry, frm = nam)

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    tree = dict()
    
    for line in input_data:
        x = re.search(r'(.*) \((\d*)\)', line)
        name = x.group(1)
        number = int(x.group(2))

        if line.find(' -> ') != -1:
            x = line.split(' -> ')
            tolink = tuple(x[1].split(', '))
            create_node(tree, name, num = number, to = tolink)
        else:
            create_node(tree, name, num = number)

    for k, v in tree.items():
        if v['fromlink'] is None:
            print(k)
            break
        

if __name__ == '__main__':
    main()

#Answer = hlhomy