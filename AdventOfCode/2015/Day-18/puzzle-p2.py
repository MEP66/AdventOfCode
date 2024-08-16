import numpy as np

DAY = '18'

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    #steps = 5
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    steps = 100

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    map0 = np.array([[1 if i == '#' else 0 for i in line] for line in input_data])
    maxrow = len(map0)
    maxcol = len(map0[0])
    map1 = np.array([[0 for _ in range(maxcol)] for _ in range(maxrow)])
    readmap0 = True

    map0[0, 0] = map0[0, maxcol-1] = map0[maxrow-1, 0] = map0[maxrow-1, maxcol-1] = 1

    for _ in range(steps):
        if readmap0:
            mapinput, mapoutput = map0, map1
        else:
            mapinput, mapoutput = map1, map0

        for ri, row in enumerate(mapinput):
            for ci, curlight in enumerate(row):
                tlrc = (max(0, ri - 1), max(0, ci - 1))
                brrc = (min(maxrow, ri + 2), min(maxcol, ci + 2))

                lightson = np.sum(mapinput[tlrc[0]:brrc[0], tlrc[1]:brrc[1]], axis = None) - curlight
                if curlight:
                    if 2 <= lightson <= 3:
                        newlightstate = 1
                    else:
                        newlightstate = 0
                else:
                    if lightson == 3:
                        newlightstate = 1
                    else:
                        newlightstate = 0
                mapoutput[ri, ci] = newlightstate

        mapoutput[0, 0] = mapoutput[0, maxcol-1] = mapoutput[maxrow-1, 0] = mapoutput[maxrow-1, maxcol-1] = 1
        readmap0 = not(readmap0)
        pass

    print(np.sum(mapoutput, axis = None))

if __name__ == '__main__':
    main()

#Answer = 781