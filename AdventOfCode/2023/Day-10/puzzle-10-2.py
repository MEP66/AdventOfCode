import re

def step(direction: str, r: int, c: int):
    ''' Take step in provided direction, return direction of next step,
    or 'end' if back to start.'''
    global pipemap

    match direction:
        case 'N':
            r -= 1
            pipe = pipemap[r][c][0]
            match pipe:
                case '|':
                    nextstep = 'N'
                    pipemap[r][c].append(1)
                case 'F':
                    nextstep = 'E'
                    pipemap[r][c].append('D')
                case '7':
                    nextstep = 'W'
                    pipemap[r][c].append('D')
                case 'S':
                    nextstep = 'end'
                    pipemap[r][c].append(1)
        case 'S':
            r += 1
            pipe = pipemap[r][c][0]
            match pipe:
                case '|':
                    nextstep = 'S'
                    pipemap[r][c].append(1)
                case 'L':
                    nextstep = 'E'
                    pipemap[r][c].append('U')
                case 'J':
                    nextstep = 'W'
                    pipemap[r][c].append('U')
                case 'S':
                    nextstep = 'end'
                    pipemap[r][c].append(1)

        case 'E':
            c += 1
            pipe = pipemap[r][c][0]
            match pipe:
                case '-':
                    nextstep = 'E'
                    pipemap[r][c].append(0)
                case 'J':
                    nextstep = 'N'
                    pipemap[r][c].append('U')
                case '7':
                    nextstep = 'S'
                    pipemap[r][c].append('D')
                case 'S':
                    nextstep = 'end'
                    pipemap[r][c].append(1)

        case 'W':
            c -= 1
            pipe = pipemap[r][c][0]
            match pipe:
                case '-':
                    nextstep = 'W'
                    pipemap[r][c].append(0)
                case 'L':
                    nextstep = 'N'
                    pipemap[r][c].append('U')
                case 'F':
                    nextstep = 'S'
                    pipemap[r][c].append('D')
                case 'S':
                    nextstep = 'end'
                    pipemap[r][c].append(1)
    return nextstep, r, c


def puzzle10():
    global pipemap
    # input data

    filename = r'./Day-10/input-10.txt'
    #filename = r'./Day-10/input-10-example.txt'


    with open(filename, 'r', encoding='utf-8') as f:
        input = f.readlines()
    
    pipemap = []
    for i, line in enumerate(input):
        elist = [[e] for e in line.strip()]
        pipemap.append(elist)
        if re.search('S', line):
            start = (i, re.search('S', line).start(0))
    print(start)
    print(pipemap)
        
    # find direction of first step

    thisstep = 'N'
    steps = 0
    r, c = start[0], start[1]
    while thisstep != 'end':
        pr, pc = r, c
        thisstep, r, c = step(thisstep, r, c)
        steps += 1
    maxsteps = steps

    insidecount = 0
    for line in pipemap:
        for i, element in enumerate(pipemap[1:-2]):
            if len(element) == 1:
                for i2, element2 in enumerate(pipemap[i+1:])


    print(steps/2)
    print(pipemap)


if __name__ == '__main__':
    puzzle10()
