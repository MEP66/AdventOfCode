from operator import xor

DAY = '03'

def calc_lsr(inplist, bitpos, type):
    inpcomp = len(inplist) / 2
    transform = list(zip(*inplist))
    compbits = (len(transform[0]) / 2)
    
    keeplist = list()
    onescount = sum(transform[bitpos])

    if type == 'oxy':
        keepbits = 1 if onescount >= compbits else 0
    else:
        keepbits = 1 if onescount < compbits else 0

    for entry in inplist:
        if entry[bitpos] == keepbits:
            keeplist.append(entry)
    
    if len(keeplist) == 1:
        result = int(''.join(str(x) for x in keeplist[0]), 2)
        return result
    else:
        result = calc_lsr(keeplist, bitpos + 1, type)
        return result


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    input_data = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            input_data.append(tuple([int(bit) for bit in line.strip()]))

    oxy = calc_lsr(input_data, 0, 'oxy')
    co2 = calc_lsr(input_data, 0, 'co2')

    print(f'Answer = {oxy * co2}')


if __name__ == '__main__':
    main()

#Answer = 3885170