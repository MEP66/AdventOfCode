

DAY = '03'

RUN = 3
RISE = 1
XSTART = 0
YSTART = 0

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    x = XSTART
    y = YSTART
    mapedge = len(input_data[0])
    treecount = 0
    for line in input_data[:-1]:
        x += RUN
        y += RISE
        if input_data[y][x % mapedge] == '#':
            treecount += 1

    print(f'Trees encountered: {treecount}')

if __name__ == '__main__':
    main()

#Answer = 252