import re


DAY = '01'


def main():
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    sum = 0

    for line in input_data:
        all_digits = re.findall(r'[0-9]', line)
        sum += int(all_digits[0] + all_digits[-1])
    print(sum)

if __name__ == '__main__':
    main()

#Answer = 53334