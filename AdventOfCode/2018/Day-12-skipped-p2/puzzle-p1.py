import re


DAY = '12'
GENERATIONS = 20
#GENERATIONS = 50000000000

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    pots = input_data[0][15:]

    gpatterns = dict()
    for line in input_data[2:]:
        pattern, result = line.split(' => ')
        gpatterns[pattern] = result

    patternmatch = set(gpatterns.keys())

    zeropos = 0
    for _ in range(GENERATIONS):
        newstring = ''
        for i in range(len(pots)+4):
            if i < 4:
                potrange = ((4-i) * '.') + pots[:(i+1)]
            elif i > len(pots)-1:
                potrange = pots[i-4:] + ((i-len(pots)+1) * '.')
            else:
                potrange = pots[i-4:i+1]

            if potrange in patternmatch:
                newstring = newstring + gpatterns[potrange]
            else:
                newstring = newstring + '.'
        
        zeroadj = 2
        for char in newstring:
            if char == '#':
                break
            else:
                zeroadj -= 1
        zeropos += zeroadj

        pots = re.sub(r'^\.+','', newstring)
        pots = re.sub(r'\.+$', '', pots)

    sum = 0
    for i, pot in enumerate(pots, (-zeropos)):
        if pot == '#':
            sum += i

    print(f'Result: {sum}')


if __name__ == '__main__':
    main()

#Answer p1 = 3405
#Answer p2 = 
