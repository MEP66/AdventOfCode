

DAY = '08'

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[x for x in line.split()] for line in f.read().splitlines()]

    program = dict()
    for i, line in enumerate(input_data):
        program[i] = {'o' : line[0], 'a' : int(line[1])}
    
    prog_end = len(program)
    modify_index = 0
    found = False

    while not found:
        while program[modify_index]['o'] == 'acc':
            modify_index += 1
        
        if program[modify_index]['o'] == 'nop':
            program[modify_index]['o'] = 'jmp'
        else:
            program[modify_index]['o'] = 'nop'
        
        pc = 0
        accumulator = 0
        executed = list()

        while pc != prog_end:
            if pc in executed or pc > prog_end:
                if program[modify_index]['o'] == 'nop':
                    program[modify_index]['o'] = 'jmp'
                else:
                    program[modify_index]['o'] = 'nop'
                modify_index += 1
                break
            else:
                executed.append(pc)
                match program[pc]['o']:
                    case 'acc':
                        accumulator += program[pc]['a']
                        pc += 1

                    case 'jmp':
                        pc += program[pc]['a']

                    case 'nop':
                        pc += 1
        else:
            print(f'Value of accumulator = {accumulator}')
            found = True

if __name__ == '__main__':
    main()

#Answer = 662