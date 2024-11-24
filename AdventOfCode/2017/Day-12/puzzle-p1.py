import re


DAY = '12'



def get_file_gen(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    get_line = get_file_gen(filename)
    IDlist = dict()

    for line in get_line:
        matches = re.findall(r'\d+', line)
        IDlist[int(matches[0])] = tuple([int(x) for x in matches[1:]])

    IDstack = [0]
    visited = list()

    while IDstack:
        id = IDstack.pop(0)
        if id not in visited:
            visited.append(id)
            IDstack.extend(IDlist[id])

    print(f'Total visited: {len(visited)}')


if __name__ == '__main__':
    main()

#Answer = 134
