import re

DAY = '01'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    sum = 0

    for line in input_data:
        sum = 0
        for cindex, char in enumerate(line):
            cindex2 = cindex + (len(line)/2)
            if cindex2 >= len(line):
                cindex2 -= len(line)
            if char == line[int(cindex2)]:
                sum += int(char)
        print(sum)

if __name__ == '__main__':
    main()

#Answer p2 = 1146