from math import inf

DAY = '07'


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        initial_pos = [int(x) for x in f.read().split(',')]

    min_pos = min(initial_pos)
    max_pos = max(initial_pos)

    min_cost = inf

    for d in range(min_pos, max_pos+1):
        cost = sum(list(map(lambda s: abs(s-d), initial_pos)))
        min_cost = min(min_cost, cost)

    print(f'Min cost: {min_cost}')

if __name__ == '__main__':
    main()

#Answer = 336040
