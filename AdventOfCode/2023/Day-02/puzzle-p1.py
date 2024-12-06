import re

DAY = '02'


def main():
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    sum = 0
    limits = {'red' : 12, 'green' : 13, 'blue' : 14}

    for line in input_data:
        possible = True

        firstsplit = line.split(':')
        gamenum = int(re.search(r'\d+', firstsplit[0]).group(0))
        grouppulls = firstsplit[1].split(';')
        for group in grouppulls:
            indivpulls = group.strip().split(',')
            for pull in indivpulls:
                data = pull.strip().split(' ')
                if int(data[0]) > limits[data[1]]:
                    possible = False
        if possible:
            sum += gamenum
    print(sum)

if __name__ == '__main__':
    main()

#Answer = 2331