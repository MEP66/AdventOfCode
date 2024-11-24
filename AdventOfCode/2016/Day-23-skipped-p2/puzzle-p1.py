

DAY = '23'

REGA_INIT = 7

def get_param(param, code, reg_dict):
    if param.lstrip('-').isdigit():
        return int(param)
    return reg_dict[param]

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        code = [[x for x in line.split(' ')] for line in f.read().splitlines()]

    registers = {'a': REGA_INIT, 'b': 0, 'c': 1, 'd': 0}

    index = 0
    while index < len(code):
        cur_line = code[index]
        match cur_line[0]:
            case 'cpy':
                val = get_param(cur_line[1], code, registers)
                if cur_line[2] in registers.keys():
                    registers[cur_line[2]] = val
                index += 1
            case 'inc':
                registers[cur_line[1]] += 1
                index += 1
            case 'dec':
                registers[cur_line[1]] -= 1
                index += 1
            case 'jnz':
                comp = get_param(cur_line[1], code, registers)
                offset = get_param(cur_line[2], code, registers)
                if comp != 0:
                    index += offset
                else:
                    index += 1
            case 'tgl':
                if cur_line[1] in registers.keys():
                    offset = index + registers[cur_line[1]]
                else:
                    offset = index + int(cur_line[1])
                if offset < len(code):
                    match code[offset][0]:
                        case 'inc':
                            code[offset][0] = 'dec'
                        case 'dec':
                            code[offset][0] = 'inc'
                        case 'jnz':
                            code[offset][0] = 'cpy'
                        case 'tgl':
                            code[offset][0] = 'inc'
                        case 'cpy':
                            code[offset][0] = 'jnz'
                        case _:
                            print('Decoding error.')
                index += 1
            case _:
                print('Decoding error.')


    print(f'Register a = {registers['a']}')

if __name__ == '__main__':
    main()

#Answer = 14065