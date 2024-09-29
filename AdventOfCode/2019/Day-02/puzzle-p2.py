from itertools import permutations


DAY = '02'

TARGET = 19690720

def getperm():
    for perm in permutations(range(100), 2):
        yield perm

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip().split(',')]
    
    perm = getperm()

    while True:
        memory = dict()
        for i, x in enumerate(input_data):
            memory[i] = x

        noun, verb = next(perm)

        memory[1] = noun
        memory[2] = verb

        ip = 0
        while memory[ip] != 99:
            if memory[ip] == 1:
                memory[memory[ip+3]] = memory[memory[ip+1]] + memory[memory[ip+2]]
            elif memory[ip] == 2:
                memory[memory[ip+3]] = memory[memory[ip+1]] * memory[memory[ip+2]]
            else:
                print(f'Error?')
            ip += 4

        if memory[0] == TARGET:
            print(f'Result is: {(100 * noun) + verb}')
            break


if __name__ == '__main__':
    main()

#Answer = 3749