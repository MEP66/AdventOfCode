from itertools import product


DAY = '07'

all_ops = ('+', '*')
super_ops = ('+', '*', '||')


def is_valid_cal_2(cal):
    tv = cal[0]
    calvals = cal[1]
    numops = len(calvals) - 1

    valid = False
    for ops in product(*[super_ops for _ in range(numops)]):
        if '||' in ops:
            left = calvals[0]
            for x in zip(ops, calvals[1:]):
                if x[0] == '||':
                    left = left + x[1]
                else:
                    left = left + ''.join(x)
                left = str(eval(left))
            if int(left) == tv:
                valid = True
                break
    return valid


def is_valid_cal(cal):
    tv = cal[0]
    calvals = cal[1]
    numops = len(calvals) - 1

    valid = False
    for ops in product(*[all_ops for _ in range(numops)]):
        equation = '('*numops + calvals[0]
        for x in zip(ops, calvals[1:], list(')' * numops)):
            equation = equation + ''.join(x)
        if eval(equation) == tv:
            valid = True
            break
    return valid


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'

    calibrations = list()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.read().splitlines():
            params = line.split(' ')
            calibrations.append([int(params[0][:-1]), [n for n in params[1:]]])

    total_calibration = 0

    for cal in calibrations:
        print(cal)
        if is_valid_cal(cal):
            total_calibration += cal[0]
        elif is_valid_cal_2(cal):
            total_calibration += cal[0]

    print(f'Total calibration = {total_calibration}')

if __name__ == '__main__':
    main()

#Answer = 91377448644679