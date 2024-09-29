from dataclasses import dataclass


DAY = '09'

@dataclass
class Code:
    opcode: int
    p1: int
    p2: int
    p3: int


def parseopcode(rawcode):
    temp = str(rawcode).zfill(5)
    return Code(opcode = int(temp[3:5]), p1 = int(temp[2]), p2 = int(temp[1]), p3 = int(temp[0]))


def get_parameter(rw, mode, ptr, rel_base, instptr, value = 0):
    if rw == 'r':
        match mode:
            case 0:
                return instptr[instptr[ptr]]
            case 1:
                return instptr[ptr]
            case 2:
                return instptr[(instptr[ptr] + rel_base)]
    else:
        match mode:
            case 0:
                instptr[instptr[ptr]] = value
            case 1:
                instptr[ptr] = value
            case 2:
                instptr[(instptr[ptr] + rel_base)] = value


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip().split(',')]

    instptr = dict()
    for i, x in enumerate(input_data):
        instptr[i] = x

    curpos = 0
    rel_base = 0
    while True:
        cc = parseopcode(instptr[curpos])

        match cc.opcode:
            case 1:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                parm2 = get_parameter('r', cc.p2, curpos + 2, rel_base, instptr)
                get_parameter('w', cc.p3, curpos + 3, rel_base, instptr, value = parm1 + parm2)
                curpos += 4
            case 2:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                parm2 = get_parameter('r', cc.p2, curpos + 2, rel_base, instptr)
                get_parameter('w', cc.p3, curpos + 3, rel_base, instptr, value = parm1 * parm2)
                curpos += 4
            case 3:
                userinput = input('Provide input: ')
                get_parameter('w', cc.p1, curpos + 1, rel_base, instptr, value = int(userinput))
                curpos += 2
            case 4:
                output = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                print(f'Output = {output}')
                curpos += 2
            case 5:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                parm2 = get_parameter('r', cc.p2, curpos + 2, rel_base, instptr)
                if parm1 != 0:
                    curpos = parm2
                else:
                    curpos += 3
            case 6:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                parm2 = get_parameter('r', cc.p2, curpos + 2, rel_base, instptr)
                if parm1 == 0:
                    curpos = parm2
                else:
                    curpos += 3
            case 7:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                parm2 = get_parameter('r', cc.p2, curpos + 2, rel_base, instptr)
                if parm1 < parm2:
                    newval = 1
                else:
                    newval = 0
                get_parameter('w', cc.p3, curpos + 3, rel_base, instptr, value = newval)
                curpos += 4
            case 8:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                parm2 = get_parameter('r', cc.p2, curpos + 2, rel_base, instptr)
                if parm1 == parm2:
                    newval = 1
                else:
                    newval = 0
                get_parameter('w', cc.p3, curpos + 3, rel_base, instptr, value = newval)
                curpos += 4
            case 9:
                parm1 = get_parameter('r', cc.p1, curpos + 1, rel_base, instptr)
                rel_base += parm1
                curpos += 2
            case 99:
                break
            case _:
                print(f'Error?')


if __name__ == '__main__':
    main()

#Answer p1 = 4006117640
#Answer p2 = 88231