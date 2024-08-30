import re

DAY = '01'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    for line in input_data:
        sum = 0
        matches = re.finditer(r'(?=(.)\1)', line + line[0])
        for item in matches:
            sum += int(item.group(1))
        print(sum)


if __name__ == '__main__':
    main()

#Answer p1 = 1203