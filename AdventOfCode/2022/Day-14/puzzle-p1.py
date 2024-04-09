import re
from collections import namedtuple
from operator import itemgetter

DAY = '14'

CR = namedtuple('CR', ['c', 'r'])
SD = namedtuple('SD', ['s', 'd'])


def form_tuples(line_in):
    c1 = re.findall('\d+', line_in)
    c2 = list(map(int, c1))
    c3 = list(CR(c2[i], c2[i+1]) for i in range(0, len(c2), 2))
    c4 = list(SD(c3[i], c3[i+1]) for i in range(0, len(c3)-1, 1))
    return c4


def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    matrix = dict()
    for line in input_data:
        datapts = form_tuples(line)
        for dp in datapts:
            if dp.s.c == dp.d.c:
                for row in range(min(dp.s.r, dp.d.r), max(dp.s.r, dp.d.r) + 1):
                    if CR(dp.s.c, row) not in matrix:
                        matrix[CR(dp.s.c, row)] = '#'
            else:
                for col in range(min(dp.s.c, dp.d.c), max(dp.s.c, dp.d.c) + 1):
                    if CR(col, dp.s.r) not in matrix:
                        matrix[CR(col, dp.s.r)] = '#'

    lastrow = max(matrix.keys(), key = itemgetter(1)).r
    inlet = CR(500, 0)
    sandcount = 0

    done = False
    while not done:
        grainpos = inlet
        nextgrain = False

        while not nextgrain and not done:
            if CR(grainpos.c, grainpos.r + 1) not in matrix:
                grainpos = CR(grainpos.c, grainpos.r + 1)
                if grainpos.r == lastrow:
                    done = True                      

            elif CR(grainpos.c - 1, grainpos.r + 1) not in matrix:
                grainpos = CR(grainpos.c - 1, grainpos.r + 1)
                if grainpos.r == lastrow:
                    done = True                      

            elif CR(grainpos.c + 1, grainpos.r + 1) not in matrix:
                grainpos = CR(grainpos.c + 1, grainpos.r + 1)
                if grainpos.r == lastrow:
                    done = True                      

            else:
                matrix[grainpos] = 'o'
                sandcount += 1
                nextgrain = True              

    print(f'Total number of grains is: {sandcount}')

if __name__ == '__main__':
    main()

#Answer = 828