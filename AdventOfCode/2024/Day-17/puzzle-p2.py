

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

                #((3 * (2**(5*3))) +     # 4 (6 - 1)  (inp #) * (2**(len(input) - (index + 1)))
                #(4 * (2**(4*3))) +     # 3 (6 - 2)
    #init_term = (4 * (2**(3*3)))      # 7,7766,7754,7747,7733,7722,7711,7700
    init_term = ((0 * (2**(2*3))) +    # 7,766,754,747,733,722,711,700
                (1 * (2**(1*3))) +     # 7,66,54,47,33,22,11,00
                (0 * (2**(0*3))))      # 7,6,4,7,3,2,1,0


    # Solution for the example problem.
    #init_term  = 0
    #for i, n in enumerate(program):
    #    init_term += (n * (2**((i+1)*3)))
    
    inst_ptr = 0
    registers['A'] = init_term
    registers['B'] = 0
    registers['C'] = 0

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
            case 2: # bst: B = operand %% 8
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
                    print(f'{init_term}    ({registers['A']}    {registers['B']}    {registers['C']})  =>  {modnum % 8}')

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
    #print(f'{init_term}    {registers['A']}    {registers['B']}    {registers['C']}    {",".join([str(x) for x in out])}')
    #print(f'Program halted.')

if __name__ == '__main__':
    main()

#Answer = 