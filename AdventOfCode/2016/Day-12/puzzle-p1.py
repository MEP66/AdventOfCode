

DAY = '12'


def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        code = [[x for x in line.split(' ')] for line in f.read().splitlines()]

    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    index = 0
    while index < len(code):
        cur_line = code[index]
        match cur_line[0]:
            case 'cpy':
                if cur_line[1].isdigit():
                    registers[cur_line[2]] = int(cur_line[1])
                    index += 1
                else:
                    registers[cur_line[2]] = registers[cur_line[1]]
                    index += 1
            case 'inc':
                registers[cur_line[1]] += 1
                index += 1
            case 'dec':
                registers[cur_line[1]] -= 1
                index += 1
            case 'jnz':
                if cur_line[1].isdigit():
                    if int(cur_line[1]) != 0:
                        index += int(cur_line[2])
                else:
                    if registers[cur_line[1]] != 0:
                        index += int(cur_line[2])
                    else:
                        index += 1
    
    print(f'Register a = {registers['a']}')

if __name__ == '__main__':
    main()

#Answer = 318003