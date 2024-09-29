from itertools import combinations

DAY = '01'

TARGETSUM = 2020

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().splitlines()]

    for combo in combinations(input_data, 3):
        if sum(combo) == TARGETSUM:
            print(f'Final product is: {combo[0] * combo[1] * combo[2]}')
            break

    pass

if __name__ == '__main__':
    main()

#Answer = 79734368