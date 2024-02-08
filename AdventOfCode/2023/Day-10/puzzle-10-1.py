import re

def step(direction: str, r: int, c: int) -> str:
    ''' Take step in provided direction, return direction of next step,
    or 'end' if back to start.'''
    global pipemap

    match direction:
        case 'N':
            r -= 1
            pipe = pipemap[r][c]
            match pipe:
                case '|':
                    nextstep = 'N'
                case 'F':
                    nextstep = 'E'
                case '7':
                    nextstep = 'W'
                case 'S':
                    nextstep = 'end'

        case 'S':
            r += 1
            pipe = pipemap[r][c]
            match pipe:
                case '|':
                    nextstep = 'S'
                case 'L':
                    nextstep = 'E'
                case 'J':
                    nextstep = 'W'
                case 'S':
                    nextstep = 'end'

        case 'E':
            c += 1
            pipe = pipemap[r][c]
            match pipe:
                case '-':
                    nextstep = 'E'
                case 'J':
                    nextstep = 'N'
                case '7':
                    nextstep = 'S'
                case 'S':
                    nextstep = 'end'

        case 'W':
            c -= 1
            pipe = pipemap[r][c]
            match pipe:
                case '-':
                    nextstep = 'W'
                case 'L':
                    nextstep = 'N'
                case 'F':
                    nextstep = 'S'
                case 'S':
                    nextstep = 'end'
    return nextstep, r, c


def puzzle10():
    global pipemap
    # input data

    filename = r'./Day-10/input-10.txt'
    #filename = r'./Day-10/input-10-example.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        pipemap = f.readlines()

    # find S
        
    for i, line in enumerate(pipemap):
        if re.search('S', line):
            start = (i, re.search('S', line).start(0))

    # find direction of first step

    thisstep = 'N'
    steps = 0
    r, c = start[0], start[1]
    while thisstep != 'end':
        thisstep, r, c = step(thisstep, r, c)
        steps += 1

    print(steps/2)


if __name__ == '__main__':
    puzzle10()

# Answer: 6599