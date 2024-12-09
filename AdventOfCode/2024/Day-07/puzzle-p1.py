from itertools import product

DAY = '07'

all_ops = ('+', '*')

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'

    calibrations = list()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.read().splitlines():
            params = line.split(' ')
            calibrations.append([int(params[0][:-1]), [n for n in params[1:]]])

    total_calibration = 0

    for cal in calibrations:
        tv = cal[0]
        calvals = cal[1]
        numops = len(calvals) - 1

        for ops in product(*[all_ops for _ in range(numops)]):
            equation = '('*numops + calvals[0]
            for x in zip(ops, calvals[1:], list(')' * numops)):
                equation = equation + ''.join(x)
            
            if eval(equation) == tv:
                total_calibration += tv
                break

    print(f'Total calibration = {total_calibration}')


if __name__ == '__main__':
    main()

#Answer = 5030892084481
