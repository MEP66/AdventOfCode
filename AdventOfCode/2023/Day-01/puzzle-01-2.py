import re

def puzzle_01():

    FILENAME = './Day-01/Input-01.txt'
    sum = 0
    digitstrs = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',
                'eight':'8', 'nine':'9', 'zero':'0'}
    searchstr = r"\d|one|two|three|four|five|six|seven|eight|nine|zero"
   
    with open(FILENAME, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

        for line in input_data:
            firstnum = re.findall(searchstr, line)[0]
            if not firstnum.isdigit():
                firstnum = digitstrs[firstnum]
            secondnum = re.findall(searchstr, line)[-1]
            if not secondnum.isdigit():
                secondnum = digitstrs[secondnum]
            sum += int(firstnum + secondnum)
    print(sum)

if __name__ == '__main__':
    puzzle_01()
