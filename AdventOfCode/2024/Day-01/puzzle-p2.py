from collections import Counter

DAY = '01'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        numpairs = [[int(x) for x in line.split()] for line in f.read().splitlines()]
            
    leftcounts = Counter([x[0] for x in numpairs])
    rightcounts = Counter([x[1] for x in numpairs])

    # Non existent Counter key returns 0.
    sumall = sum([leftcounts[num] * num * rightcounts[num] for num in leftcounts])

    print(f'Result: {sumall}')

if __name__ == '__main__':
    main()

#Answer = 23228917