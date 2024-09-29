import re
from collections import defaultdict


DAY = '07'
    
TARGET = 'shiny gold'

def get_all_bags(style, allbags):
    count = 1
    if allbags[style]['contains'] is not None:
        for s, c in allbags[style]['contains'].items():
            count += c * get_all_bags(s, allbags)
    return count


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    all_bags = defaultdict(lambda: {'contains' : dict(), 'contained_in' : dict()})

    for line in input_data:
        cur_bag, temp = re.search(r'(.+) bags contain (.+)\.', line).groups()
        temp = [re.search(r'(\d+|no) (.*) bags*', x).groups() for x in temp.split(', ')]

        if temp[0][0] == 'no':
            all_bags[cur_bag]['contains'] = None
        else:
            for num, style in temp:
                all_bags[cur_bag]['contains'][style] = int(num)
                all_bags[style]['contained_in'][cur_bag] = 0
    
    print(f'Number that contained in my bag: {get_all_bags(TARGET, all_bags) - 1}')


if __name__ == '__main__':
    main()

#Answer = 5635