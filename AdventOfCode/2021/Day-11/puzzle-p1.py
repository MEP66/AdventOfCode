from math import inf


DAY = '11'

STEPS = 100

def inc_region(topleft, botright, omap):
    rowstart = max(topleft[0], 0)
    rowend = min(botright[0], len(omap)-1)
    colstart = max(topleft[1], 0)
    colend = min(botright[1], len(omap[0])-1)
    for row in range(rowstart, rowend+1):
        for col in range(colstart, colend+1):
            omap[row][col] += 1


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        octo_map = [[int(x) for x in line] for line in f.read().splitlines()]

    max_row = len(octo_map)
    max_col = len(octo_map[0])

    total_flashes = 0

    for _ in range(STEPS):
        inc_region((0,0), (max_row, max_col), octo_map)
        while True:
            flashfound = False
            for ri, row in enumerate(octo_map):
                for ci, octo in enumerate(row):
                    if 10 <= octo < inf:
                        inc_region((ri-1, ci-1), (ri+1, ci+1), octo_map)
                        octo_map[ri][ci] = inf
                        total_flashes += 1
                        flashfound = True
            if not flashfound:
                break

        for ri, row in enumerate(octo_map):
            for ci, octo in enumerate(row):
                if octo == inf:
                    octo_map[ri][ci] = 0

        
    print(f'Total flashes: {total_flashes}')


if __name__ == '__main__':
    main()

#Answer = 1719