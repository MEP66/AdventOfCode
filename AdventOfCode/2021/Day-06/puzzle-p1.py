from collections import Counter


DAY = '06'

NUMDAYS = 80

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        fishes = [int(x) for x in f.read().split(',')]

    fishcounts = dict(Counter(fishes))
    for x in range(9):
        if x not in fishcounts:
            fishcounts[x] = 0
    
    for _ in range(NUMDAYS):
        temp6 = temp8 = fishcounts[0]
        fishcounts[0] = fishcounts[1]
        fishcounts[1] = fishcounts[2]
        fishcounts[2] = fishcounts[3]
        fishcounts[3] = fishcounts[4]
        fishcounts[4] = fishcounts[5]
        fishcounts[5] = fishcounts[6]
        fishcounts[6] = fishcounts[7] + temp6
        fishcounts[7] = fishcounts[8]
        fishcounts[8] = temp8


    print(f'Total fish: {sum(fishcounts.values())}')


if __name__ == '__main__':
    main()

#Answer = 350917
