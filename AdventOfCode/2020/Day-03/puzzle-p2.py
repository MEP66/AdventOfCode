

DAY = '03'

SLOPES = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
XSTART = 0
YSTART = 0


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    mapedge = len(input_data[0])
    result = 1

    for slope in SLOPES:
        run = slope[0]
        rise = slope[1]
        x = XSTART + run
        y = YSTART + rise

        treecount = 0

        while y < len(input_data):
            if input_data[y][x % mapedge] == '#':
                treecount += 1
            x += run
            y += rise

        result *= treecount

    print(f'Trees encountered: {(result)}')

if __name__ == '__main__':
    main()

#Answer = 2608962048