import re
from collections import defaultdict


DAY = '07'
    
TARGET = 'shiny gold'

def get_all_bags(style, containslist, allbags):
        containslist.add(style)
        for s, _ in allbags[style]['contained_in'].items():
            get_all_bags(s, containslist, allbags)


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

    contains_mine = set()
    for s, c in all_bags.items():
        if c['contains'] is not None:
            if TARGET in c['contains'].keys():
                get_all_bags(s, contains_mine, all_bags)
    

    print(f'Number that contain my bag: {len(contains_mine)}')


if __name__ == '__main__':
    main()

#Answer = 326