import re

DAY = '12'


def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read()

    numbers = re.findall(r'-?\d+', input_data)
    total_sum = 0
    for num in numbers:
         total_sum += int(num)

    print(total_sum)

if __name__ == '__main__':
    main()

#Answer = 119433
