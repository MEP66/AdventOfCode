

DAY = '05'

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    occupiedseats = list()
    for line in input_data:
        row = line[:7].replace('F', '0').replace('B', '1')
        col = line[7:].replace('L', '0').replace('R', '1')

        occupiedseats.append((int(row, 2), int(col, 2)))

    for row in range(2, 125):
        for col in range(8):
            if ((row, col) not in occupiedseats and
                (row-1, col) in occupiedseats and
                (row+1, col) in occupiedseats):
                print(f'My seat value is: row={row}, col={col}: value={(row * 8) + col}')

if __name__ == '__main__':
    main()

#Answer = 705