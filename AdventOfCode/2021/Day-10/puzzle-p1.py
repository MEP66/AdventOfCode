

DAY = '10'

brackets = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
scoring = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    score = 0
    for line in input_data:
        stack = list()
        for char in line:
            if char in brackets:
                stack.append(char)
            else:
                lastpop = stack.pop(-1)
                if brackets[lastpop] != char:
                    score += scoring[char]
                    break
                else:
                    if len(stack) == 0:
                        break

    
    print(f'Score: {score}')


if __name__ == '__main__':
    main()

#Answer = 215229