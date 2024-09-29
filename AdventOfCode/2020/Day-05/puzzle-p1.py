

DAY = '05'

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    highestseat = 0
    for line in input_data:
        row = line[:7].replace('F', '0').replace('B', '1')
        col = line[7:].replace('L', '0').replace('R', '1')

        highestseat = max(highestseat, (int(row, 2) * 8) + int(col, 2))

    print(f'Highest seat value is: {highestseat}')

if __name__ == '__main__':
    main()

#Answer = 822