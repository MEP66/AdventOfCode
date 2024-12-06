import re


DAY = '01'


def main():
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2023/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    sum = 0
    digitstrs = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',
                'eight':'8', 'nine':'9', 'zero':'0'}
    searchstr = r"\d|one|two|three|four|five|six|seven|eight|nine|zero"

    for line in input_data:
        matches = re.findall(searchstr, line)
        firstnum = matches[0]
        if not firstnum.isdigit():
            firstnum = digitstrs[firstnum]
        secondnum = matches[-1]
        if not secondnum.isdigit():
            secondnum = digitstrs[secondnum]
        sum += int(firstnum + secondnum)
    print(sum)

if __name__ == '__main__':
    main()

#Answer = 52834