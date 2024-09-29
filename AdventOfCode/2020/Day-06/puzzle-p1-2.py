

DAY = '06'

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        batches = [[set(x) for x in line.split()] for line in f.read().split('\n\n')]

    totalsum = sum(len(set.union(*batch)) for batch in batches)
    print(f'Answer:  {totalsum}')


if __name__ == '__main__':
    main()

#Answer = 6443
