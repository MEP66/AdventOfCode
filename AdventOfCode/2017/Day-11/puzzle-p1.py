# https://www.redblobgames.com/grids/hexagons/


DAY = '11'


hdir = {'n': (0, 1, -1), 's': (0, -1, 1),
        'ne': (1, 0, -1),'sw': (-1, 0, 1),
        'nw': (1, -1, 0), 'se': (-1, 1, 0)}

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        path = [d for d in f.read().strip().split(',')]

    curloc = [0, 0, 0]

    for d in path:
        curloc = [a + b for a, b in zip(curloc, hdir[d])]

    finaldist = int(sum([abs(p) for p in curloc])/2)
    print(f'Final distance is: {finaldist}')


if __name__ == '__main__':
    main()

#Answer: 685