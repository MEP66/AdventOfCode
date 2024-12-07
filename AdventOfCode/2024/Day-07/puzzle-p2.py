

DAY = '07'

op_cnvr = {'0': '+', '1': '*', '2': '||'}

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


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
        tv = cal[0]
        calvals = cal[1]
        numops = len(calvals) - 1

        for mask in range(3**numops):

            ops = [op_cnvr[b] for b in list(ternary(mask).zfill(numops))]
            temp_cv = [calvals[0]]
            temp_ops = list()

            for i, op in enumerate(ops):
                if op == '||':
                    temp_cv[-1] = temp_cv[-1] + calvals[i+1]
                else:
                    temp_cv.append(calvals[i+1])
                    temp_ops.append(ops[i])

            equation = '('*len(temp_ops) + temp_cv[0]
            for x in zip(temp_ops, temp_cv[1:], list(')' * len(temp_ops))):
                equation = equation + ''.join(x)
            
            if eval(equation) == tv:
                total_calibration += tv
                break


    print(f'Total calibration = {total_calibration}')


if __name__ == '__main__':
    main()
