

DAY = '01'

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().splitlines()]

    totalmass = 0
    for f in input_data:
        fmass = int(f/3) - 2
        totalmass += fmass

    print(f'Total mass is: {totalmass}')

if __name__ == '__main__':
    main()

#Answer = 3412531