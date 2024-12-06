from collections import namedtuple


DAY = '18'


def main():

    filename = fr'./AdventOfCode/2023/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input.txt'
    
    inst = namedtuple('inst', 'dir dist color')

    input_data = list()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.read().splitlines():
            params = line.split(' ')
            input_data.append(inst(params[0], int(params[1]), params[2]))

    # Get chart orientation
    
    allsteps = list()
    rindex, cindex = 0, 0
    for i, item in enumerate(input_data):
        match item.dir:
            case 'U':
                rindex -= item.dist
            case 'R':
                cindex += item.dist
            case 'D':
                rindex += item.dist
            case 'L':
                cindex -= item.dist
        allsteps.append((i, (rindex, cindex)))

    rmin = min([item[1][0] for item in allsteps])
    rmax = max([item[1][0] for item in allsteps])
    cmin = min([item[1][1] for item in allsteps])
    cmax = max([item[1][1] for item in allsteps])

    numrows = abs(rmin) + abs(rmax) + 1
    numcols = abs(cmin) + abs(cmax) + 1

    for item in allsteps:
        if item[1][0] == rmin:
            irmin = item[0]
            break
    for item in allsteps:
        if item[1][1] == cmin:
            icmin = item[0]
            break
    
    del allsteps

    digmap = list()
    for _ in range(numrows):
        digmap.append(list('.' * numcols))

    digri = irmin
    digci = icmin
    digmap[digri][digci] = '#'

    for item in input_data:
        match item.dir:
            case 'U':
                for _ in range(item.dist):
                    digri -= 1
                    digmap[digri][digci] = '#'
            case 'D':
                for _ in range(item.dist):
                    digri += 1
                    digmap[digri][digci] = '#'
            case 'R':
                for _ in range(item.dist):
                    digci += 1
                    digmap[digri][digci] = '#'
            case 'L':
                for _ in range(item.dist):
                    digci -= 1
                    digmap[digri][digci] = '#'

    print(rmin, rmax, cmin, cmax)
    print(irmin, icmin)

if __name__ == '__main__':
    main()

