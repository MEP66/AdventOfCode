import re
from collections import defaultdict


DAY = '03'

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        params = [[int(x) for x in re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups()]
                    for line in f.read().splitlines()]
    
    fabmap = defaultdict(lambda: 0)

    for (_, sc, sr, nc, nr) in params:
        for r in range(sr, sr + nr):
            for c in range(sc, sc + nc):
                fabmap[(r, c)] += 1

    count = 0
    for v in fabmap.values():
        if v >= 2:
            count += 1

    print(f'Result: {count}')


if __name__ == '__main__':
    main()

#Answer = 108961