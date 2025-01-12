
# Solution for the example problem.
#init_term  = 03
#for i, n in enumerate(program):
#    init_term += (n * (2**((i+1)*3)))


DAY = '17'

def eval_stm(A_init, B_init, C_init, program):
    inst_ptr = 0
    registers = {'A': A_init, 'B': B_init, 'C': C_init}
    out = list()


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
    return out


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    B = C = 0
    program = [int(x) for x in input_data[4].split(': ')[1].split(',')]

    # First figure out how many input octects product the proper length output.

    place_count = 0
    while True:
        A = int('1' + ('0' * place_count), 8)
        if len(eval_stm(A, B, C, program)) == len(program):
            break
        place_count += 1
    
    A_target = ''
    for i in range(place_count, -1, -1):
        d = 0
        while True:
            A = int(A_target + str(d) + ('0' * i), 8)
            if A != 0:
                if eval_stm(A, B, C, program)[i] == program[i]:
                    A_target += str(d)
                    break
            d += 1
    
    print(f'A initializtion value = {int(A_target, 8)}, octal={A_target}')


if __name__ == '__main__':
    main()

#Answer = 266932601404433 (base 8: 7454302670536021)