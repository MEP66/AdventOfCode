

DAY = '01'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        numpairs = [[int(x) for x in line.split()] for line in f.read().splitlines()]
            
    leftnums = [x[0] for x in numpairs]
    leftnums.sort()
    rightnums = [x[1] for x in numpairs]
    rightnums.sort()

    sumdist = sum([abs(l-r) for l, r in zip(leftnums, rightnums)])

    print(f'Result: {sumdist}')

if __name__ == '__main__':
    main()

#Answer = 1889772