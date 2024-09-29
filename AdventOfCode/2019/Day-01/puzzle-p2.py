

DAY = '01'

def calc_fuel(m):
    fmass = (int(m/3) - 2)

    if fmass > 0:
        total = fmass + calc_fuel(fmass)
        return total
    else:
        return 0

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().splitlines()]

    totalmass = 0
    for f in input_data:
        totalmass += calc_fuel(f)

    print(f'Total mass is: {totalmass}')

if __name__ == '__main__':
    main()

#Answer = 5115927