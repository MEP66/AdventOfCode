import re
from collections import Counter

DAY = '04'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    input_data = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            x = re.search(r'(.+)-(\d+)\[(.+)\]', line)
            input_data.append((''.join(x[1].split('-')), int(x[2]), x[3]))
    
    sum = 0
    for entry in input_data:
        counts = list(Counter(entry[0]).items())
        counts.sort(key = lambda x: (-x[1], x[0]))
        counts = counts[:5]
        if ''.join([x[0] for x in counts]) == entry[2]:
            sum += entry[1]

    print(sum)


if __name__ == '__main__':
    main()

#Answer = 158835
