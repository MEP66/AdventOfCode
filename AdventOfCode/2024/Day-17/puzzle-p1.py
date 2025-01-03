

DAY = '17'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    registers = {'A': None, 'B': None, 'C': None}
    registers['A'] = int(input_data[0].split(': ')[1])
    registers['B'] = int(input_data[1].split(': ')[1])
    registers['C'] = int(input_data[2].split(': ')[1])

    program = [int(x) for x in input_data[4].split(': ')[1].split(',')]
    out = list()

    inst_ptr = 0
    while True:
        opcode = program[inst_ptr]
        operand = program[inst_ptr + 1]

        match opcode:
            case 0: # adv: A = int(A / 2**operand)
                error = False
                match operand:
                    case 0|1|2|3:
                        power = operand
                    case 4:
                        power = registers['A']
                    case 5:
                        power = registers['B']
                    case 6:
                        power = registers['C']
                    case 7:
                        print(f'Error.')
                        error = True
                if not error:
                    registers['A'] = int(registers['A'] / (2**power))
                inst_ptr += 2
            case 1: # bxl: B = B XOR operand
                registers['B'] = registers['B'] ^ operand
                inst_ptr += 2
            case 2: # bst: B = operand % 8
                error = False
                match operand:
                    case 4:
                        modnum = registers['A']
                    case 5:
                        modnum = registers['B']
                    case 6:
                        modnum = registers['C']
                    case _:
                        print(f'Error')
                        error = True
                if not error:
                    registers['B'] = modnum % 8
                inst_ptr += 2
            case 3: # jnz: jump to operand if A not 0
                if registers['A'] != 0:
                    match operand:
                        case 0|1|2|3:
                            inst_ptr = operand
                        case _:
                            print(f'Error')
                else:
                    inst_ptr += 2
            case 4: # bxc: B = B XOR C
                registers['B'] = registers['B'] ^ registers['C']
                inst_ptr += 2
            case 5: # out: operand % 8
                error = False
                match operand:
                    case 0|1|2|3:
                        modnum = operand
                    case 4:
                        modnum = registers['A']
                    case 5:
                        modnum = registers['B']
                    case 6:
                        modnum = registers['C']
                    case _:
                        print(f'Error')
                        error = True
                if not error:
                    out.append(modnum % 8)
                inst_ptr += 2
            case 6: # adv: B = int(A / 2**operand) 
                error = False
                match operand:
                    case 0|1|2|3:
                        power = operand
                    case 4:
                        power = registers['A']
                    case 5:
                        power = registers['B']
                    case 6:
                        power = registers['C']
                    case 7:
                        print(f'Error.')
                        error = True
                if not error:
                    registers['B'] = int(registers['A'] / (2**power))
                inst_ptr += 2
            case 7:# cdv: C = int(A / 2**operand) 
                error = False
                match operand:
                    case 0|1|2|3:
                        power = operand
                    case 4:
                        power = registers['A']
                    case 5:
                        power = registers['B']
                    case 6:
                        power = registers['C']
                    case 7:
                        print(f'Error.')
                        error = True
                if not error:
                    registers['C'] = int(registers['A'] / (2**power))
                inst_ptr += 2
        if inst_ptr >= len(program):
            break
    if out:
        print(f'Output: {",".join([str(x) for x in out])}')
    print(f'Program halted.')

if __name__ == '__main__':
    main()

#Answer = 2,1,4,7,6,0,3,1,4