

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip().split(',')]
    
    opcodes = dict()
    for i, x in enumerate(input_data):
        opcodes[i] = x
    
    opcodes[1] = 12
    opcodes[2] = 2

    curpos = 0
    while opcodes[curpos] != 99:
        if opcodes[curpos] == 1:
            opcodes[opcodes[curpos+3]] = opcodes[opcodes[curpos+1]] + opcodes[opcodes[curpos+2]]
        elif opcodes[curpos] == 2:
            opcodes[opcodes[curpos+3]] = opcodes[opcodes[curpos+1]] * opcodes[opcodes[curpos+2]]
        else:
            print(f'Error?')
        curpos += 4

    print(f'Position 0 value: {opcodes[0]}')


if __name__ == '__main__':
    main()

#Answer = 6730673