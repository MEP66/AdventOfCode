from dataclasses import dataclass
from itertools import permutations, cycle


DAY = '07'

@dataclass
class Code:
    opcode: int
    p1: int
    p2: int
    p3: int


class Amp:
    def __init__(self, computer):
        self._instptr = computer.copy()
        self._curpos = 0
        self._firstinput = True
        self._status = 'initialized'
        self._output = 0

    def parse_opcode(self, rawcode):
        _temp = str(rawcode).zfill(5)
        return Code(opcode = int(_temp[3:5]), p1 = int(_temp[2]), p2 = int(_temp[1]), p3 = int(_temp[0]))

    def execute_code(self, phase_in, signal_in):
        while True:
            cc = self.parse_opcode(self._instptr[self._curpos])
            if cc.opcode not in [3, 4, 99]:
                parm1 = self._instptr[self._curpos+1] if cc.p1 else self._instptr[self._instptr[self._curpos+1]]
                parm2 = self._instptr[self._curpos+2] if cc.p2 else self._instptr[self._instptr[self._curpos+2]]
            match cc.opcode:
                case 1:
                    self._instptr[self._instptr[self._curpos+3]] = parm1 + parm2
                    self._curpos += 4
                case 2:
                    self._instptr[self._instptr[self._curpos+3]] = parm1 * parm2
                    self._curpos += 4
                case 3:
                    if self._firstinput:
                        self._instptr[self._instptr[self._curpos+1]] = phase_in
                        self._firstinput = False
                    else:
                        self._instptr[self._instptr[self._curpos+1]] = signal_in
                    self._curpos += 2
                case 4:
                    self._output = self._instptr[self._instptr[self._curpos+1]]
                    self._curpos += 2
                    self._status = 'paused'
                    break
                case 5:
                    if parm1 != 0:
                        self._curpos = parm2
                    else:
                        self._curpos += 3
                case 6:
                    if parm1 == 0:
                        self._curpos = parm2
                    else:
                        self._curpos += 3
                case 7:
                    if parm1 < parm2:
                        self._instptr[self._instptr[self._curpos+3]] = 1
                    else:
                        self._instptr[self._instptr[self._curpos+3]] = 0
                    self._curpos += 4
                case 8:
                    if parm1 == parm2:
                        self._instptr[self._instptr[self._curpos+3]] = 1
                    else:
                        self._instptr[self._instptr[self._curpos+3]] = 0
                    self._curpos += 4
                case 99:
                    self._status = 'halt'
                    break
                case _:
                    print(f'Unexpected Opcode Error')
                    self._status = 'error'
                    break
        return((self._status, self._output))


def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip().split(',')]

    computer = dict()
    for i, x in enumerate(input_data):
        computer[i] = x

    max_output = 0

    for phase_inputs in permutations([5, 6, 7, 8, 9], 5):

        A = Amp(computer)
        B = Amp(computer)
        C = Amp(computer)
        D = Amp(computer)
        E = Amp(computer)
        all_amps = [A, B, C, D, E]

        sig_output = 0

        while True:
            for amp, pi in cycle(zip(all_amps, phase_inputs)):      
                status, sig_output = amp.execute_code(pi, sig_output)
                if status == 'halt' and amp is E:
                    max_output = max(max_output, sig_output)
                    break
            else:
                continue
            break

    print(f'Max output is: {max_output}')


if __name__ == '__main__':
    main()

#Answer = 58285150