


def main():


    def takestep(r, c, map, stepqueue):
        try:
            if map[r][c] == '.':
                map[r][c] = '0'
                stepqueue.append((r, c))
        except:
            pass


    # Fetch data

    filename = r'./Day-21/input-example.txt'
    filename = r'./Day-21/input.txt'

    NUMSTEPS = 26501365

    with open(filename, 'r', encoding='utf-8') as f:
        gardenmap = [list(line.strip()) for line in f]

    # Find starting point.
    
    for r, line in enumerate(gardenmap):
        for c, item in enumerate(line):
            if item == 'S':
                startpoint = (r, c)
    
    # Process steps
    
    stepstoprocess = [startpoint]

    gardenmap[startpoint[0]][startpoint[1]] = '0'
    for _ in range(NUMSTEPS):
        for _ in range(len(stepstoprocess)):
            r = stepstoprocess[0][0]
            c = stepstoprocess[0][1]
            del stepstoprocess[0]

            gardenmap[r][c] = '.'
            takestep(r-1, c, gardenmap, stepstoprocess)
            takestep(r, c+1, gardenmap, stepstoprocess)
            takestep(r+1, c, gardenmap, stepstoprocess)
            takestep(r, c-1, gardenmap, stepstoprocess)

    # Count steps reached

    sum = 0
    for line in gardenmap:
        for plot in line:
            if plot == '0':
                sum += 1

    print(sum)



if __name__ == '__main__':
    main()

# Answer = 3594