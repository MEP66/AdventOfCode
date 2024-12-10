import re


DAY = '02'


def main():
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    sum = 0

    for line in input_data:
        maxballs = {'red' : 0, 'green' : 0, 'blue' : 0}

        for group in line.split(': ')[1].split(';'):
            for pull in group.strip().split(','):
                number, color = pull.strip().split(' ')
                maxballs[color] = max(maxballs[color], int(number))

        sum += maxballs['red'] * maxballs['green'] * maxballs['blue']
    print(sum)

if __name__ == '__main__':
    main()

#Answer = 71585