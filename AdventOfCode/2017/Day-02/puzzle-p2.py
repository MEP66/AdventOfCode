import re
from itertools import combinations


DAY = '02'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    checksum = 0
    for line in input_data:
        numbers = [int(x) for x in re.findall(r'\d+', line)]
        combos = combinations(numbers, 2)
        for pairs in combos:
            q, r = divmod(max(pairs), min(pairs))
            if r == 0:
                checksum += q
                break

    print(checksum)


if __name__ == '__main__':
    main()

#Answer = 221
