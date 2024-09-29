

DAY = '08'

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        #input_data = [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]
        input_data = [line.split() for line in f.read().splitlines()]
        input_data = [(x[0], int(x[1])) for x in input_data]

    program = dict()

    for i, line in enumerate(input_data):
        program[i] = {'o' : line[0], 'a' : int(line[1])}
    
    pc = 0
    accumulator = 0
    executed = list()

    while True:
        if pc in executed:
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
    
    print(f'Value of accumulator = {accumulator}')

if __name__ == '__main__':
    main()

#Answer = 1832