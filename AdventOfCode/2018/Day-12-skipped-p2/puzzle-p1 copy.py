import re


DAY = '12'
GENERATIONS = 20
GENERATIONS = 50000000000

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    pots = input_data[0][15:]
    pots = re.sub(r'\.', '0', pots)
    pots = re.sub(r'\#', '1', pots)

    gpatterns = dict()
    for line in input_data[2:]:
        line = re.sub(r'\.', '0', line)
        line = re.sub(r'\#', '1', line)
        pattern, result = line.split(' => ')
        gpatterns[pattern] = result

    zeropos = 0

    for _ in range(GENERATIONS):
        pots = '0000' + pots + '0000'
        newstring = []
        for i in range(len(pots)-4):
            newstring.append(gpatterns[pots[i:i+5]])

        zeroadj = 2
        for i, char in enumerate(newstring):
            if char == '1':
                break
            else:
                newstring.pop(i)
                zeroadj -= 1
        zeropos += zeroadj

        while True:
            char = newstring[-1]
            if char == '0':
                newstring.pop(-1)
            else:
                break

        pots = ''.join(newstring)

    sum = 0
    for i, pot in enumerate(pots, (-zeropos)):
        if pot == '1':
            sum += i

    print(f'Result: {sum}')


if __name__ == '__main__':
    main()

#Answer p1 = 3405
#Answer p2 = 
