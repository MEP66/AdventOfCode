import re
from collections import defaultdict

DAY = '08'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    regs = defaultdict(lambda: 0)

    largestever = 0
    for line in input_data:
        match = re.search(r'^(.+) (inc|dec) (-?\d+) if (.+?) (.+)', line)
        operand = match.group(1)
        operator = match.group(2)
        value = int(match.group(3))
        testvar = match.group(4)
        testexp = match.group(5)

        testval = regs[testvar]
        if eval(str(testval) + testexp):
            if operator == 'inc':
                regs[operand] += value
            else:
                regs[operand] -= value

        largestever = max(largestever, max(regs.values()))

    print(f'Largest register value = {max(regs.values())}')
    print(f'largest register value ever held = {largestever}')


if __name__ == '__main__':
    main()

#Answer p1 = 5143
#Answer p2 = 6209