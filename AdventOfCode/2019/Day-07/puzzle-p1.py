from dataclasses import dataclass
from itertools import permutations


DAY = '07'

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

    computer = dict()
    for i, x in enumerate(input_data):
        computer[i] = x

    max_output = 0

    for phase_inputs in permutations([0, 1, 2, 3, 4], 5):
        prev_output = 0

        for phase_input in phase_inputs:
            curpos = 0
            firstinput = True 
            instptr = computer.copy()

            while True:
                cc = parseopcode(instptr[curpos])
                if cc.opcode not in [3, 4, 99]:
                    parm1 = instptr[curpos+1] if cc.p1 else instptr[instptr[curpos+1]]
                    parm2 = instptr[curpos+2] if cc.p2 else instptr[instptr[curpos+2]]
                match cc.opcode:
                    case 1:
                        instptr[instptr[curpos+3]] = parm1 + parm2
                        curpos += 4
                    case 2:
                        instptr[instptr[curpos+3]] = parm1 * parm2
                        curpos += 4
                    case 3:
                        if firstinput:
                            instptr[instptr[curpos+1]] = phase_input
                            firstinput = not(firstinput)
                        else:
                            instptr[instptr[curpos+1]] = prev_output
                        curpos += 2
                    case 4:
                        prev_output = instptr[instptr[curpos+1]]
                        curpos += 2
                    case 5:
                        if parm1 != 0:
                            curpos = parm2
                        else:
                            curpos += 3
                    case 6:
                        if parm1 == 0:
                            curpos = parm2
                        else:
                            curpos += 3
                    case 7:
                        if parm1 < parm2:
                            instptr[instptr[curpos+3]] = 1
                        else:
                            instptr[instptr[curpos+3]] = 0
                        curpos += 4
                    case 8:
                        if parm1 == parm2:
                            instptr[instptr[curpos+3]] = 1
                        else:
                            instptr[instptr[curpos+3]] = 0
                        curpos += 4
                    case 99:
                        break
                    case _:
                        print(f'Unexpected Opcode Error')

        max_output = max(max_output, prev_output)
    
    print(f'Max output is: {max_output}')


if __name__ == '__main__':
    main()

#Answer = 255590