from dataclasses import dataclass
import re

DAY = '23'

@dataclass
class Inst:
    op: str
    reg: str
    offset: int

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    instructions = dict()
    for entrynum, line in enumerate(input_data, 1):
        linedata = re.split(' |, ', line)
        operand = linedata[0]

        match operand:
            case 'jmp':
                offset = int(linedata[1])
                register = None
            case 'jio' | 'jie':
                offset = int(linedata[2])
                register = linedata[1]
            case _:
                offset = None
                register = linedata[1]

        instructions[entrynum] = Inst(operand, register, offset)

    regs = {'a' : 1, 'b' : 0}
    inst_index = 1
    max_index = len(instructions)

    while 1 <= inst_index <= max_index:
        cur_inst = instructions[inst_index]

        match cur_inst.op:
            case 'jmp':
                inst_index += cur_inst.offset
            case 'jio':
                if regs[cur_inst.reg] == 1:
                    inst_index += cur_inst.offset
                else:
                    inst_index += 1
            case 'jie':
                if regs[cur_inst.reg] % 2 == 0:
                    inst_index += cur_inst.offset
                else:
                    inst_index += 1
            case 'inc':
                regs[cur_inst.reg] += 1
                inst_index += 1
            case 'tpl':
                regs[cur_inst.reg] = regs[cur_inst.reg] * 3
                inst_index += 1
            case 'hlf':
                regs[cur_inst.reg] = regs[cur_inst.reg] / 2
                inst_index += 1
    print(regs['b'])

if __name__ == '__main__':
    main()

#Answer = 247