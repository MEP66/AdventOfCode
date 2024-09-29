from dataclasses import dataclass


DAY = '05'

@dataclass
class Code:
    opcode: int
    p1: int
    p2: int
    p3: int


def parseopcode(rawcode):
    temp = str(rawcode).zfill(5)
    return Code(opcode = int(temp[3:5]), p1 = int(temp[2]), p2 = int(temp[1]), p3 = int(temp[0]))

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip().split(',')]

    instptr = dict()
    for i, x in enumerate(input_data):
        instptr[i] = x

    curpos = 0
    while True:
        cc = parseopcode(instptr[curpos])
        if cc.opcode == 1:
            parm1 = instptr[curpos+1] if cc.p1 else instptr[instptr[curpos+1]]
            parm2 = instptr[curpos+2] if cc.p2 else instptr[instptr[curpos+2]]
            instptr[instptr[curpos+3]] = parm1 + parm2
            curpos += 4
        elif cc.opcode == 2:
            parm1 = instptr[curpos+1] if cc.p1 else instptr[instptr[curpos+1]]
            parm2 = instptr[curpos+2] if cc.p2 else instptr[instptr[curpos+2]]
            instptr[instptr[curpos+3]] = parm1 * parm2
            curpos += 4
        elif cc.opcode == 3:
            userinput = input('Provide input: ')
            instptr[instptr[curpos+1]] = int(userinput)
            curpos += 2
        elif cc.opcode == 4:
            print(f'Output = : {instptr[instptr[curpos+1]]}')
            curpos += 2
        elif cc.opcode == 99:
            break
        else:
            print(f'Error?')


if __name__ == '__main__':
    main()

#Answer = 16225258