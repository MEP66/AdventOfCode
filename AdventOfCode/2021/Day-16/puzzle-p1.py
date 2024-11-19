

DAY = '16'


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    bits = list()
    for c in input_data:
        bits.extend(list(f'{int("0x"+c, 16):0>{4}b}'))

    version_sum = 0
    i = 0
    state_stack = [('get_bpc', 1)]

    while state_stack:
        cmd, count = state_stack.pop(-1)

        match cmd:
            case 'get_bpc':
                count -= 1
                if count != 0:
                    state_stack.append(('get_bpc', count))
                version = int(''.join(bits[i:i+3]), 2)
                type = int(''.join(bits[i+3:i+6]), 2)
                i += 6
                if type == 4:
                    literal = list()
                    while True:
                        literal.extend(bits[i+1:i+5])
                        if bits[i] == '0':
                            version = int(''.join(literal), 2)
                            version_sum += version
                            i += 5
                            break
                        i += 5
                else:
                    op_ltype = bits[i]
                    i += 1
                    if op_ltype == '0':
                        op_len = int(''.join(bits[i:i+15]), 2)
                        i += 15
                        state_stack.append(('get_bbc', op_len))
                    else:
                        op_len = int(''.join(bits[i:i+11]), 2)
                        i += 11
                        state_stack.append(('get_bpc', op_len))
            case 'get_bbc':
                version = int(''.join(bits[i:i+3]), 2)
                type = int(''.join(bits[i+3:i+6]), 2)
                i += 6
                bc = 6
                if type == 4:
                    literal = list()
                    while True:
                        literal.extend(bits[i+1:i+5])
                        if bits[i] == '0':
                            version = int(''.join(literal), 2)
                            version_sum += version
                            i += 5
                            bc += 5
                            break
                        i += 5
                        bc += 5
                    count -= bc
                    if count > 0:
                        state_stack.append(('get_bbc', count))
                else:
                    print(f'Operation after bit count')
        pass
    print(f'Sum: {version_sum}')

if __name__ == '__main__':
    main()
