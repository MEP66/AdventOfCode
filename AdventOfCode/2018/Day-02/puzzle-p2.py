from itertools import combinations


DAY = '02'


def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [x for x in f.read().splitlines()]

    generator_exp = combinations(input_data, 2)

    for combo in generator_exp:
        in_common = [c for i, c in enumerate(combo[0]) if c == combo[1][i]]
        if len(in_common) == len(combo[0]) - 1:
            print(f'Result: {''.join(in_common)}')
            break


if __name__ == '__main__':
    main()

#Answer = ymdrchgpvwfloluktajxijsqb