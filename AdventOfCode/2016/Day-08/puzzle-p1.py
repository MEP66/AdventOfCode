import re


DAY = '08'

WIDTH = 50
HEIGHT = 6


def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    displaymap = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for line in input_data:
        params = [int(x) for x in re.findall(r'\d+', line)]
        operator = re.search(r'rect|row|column', line)

        match operator.group(0):
            case 'rect':
                cols, rows = params[0], params[1]
                for r in range(rows):
                    for c in range(cols):
                        displaymap[r][c] = 1

            case 'row':
                row, shiftnum = params[0], params[1]
                for _ in range(shiftnum):
                    rollover = displaymap[row][WIDTH - 1]
                    for c in range(WIDTH-1, 0, -1):
                        displaymap[row][c] = displaymap[row][c-1]
                    displaymap[row][0] = rollover

            case 'column':
                column, shiftnum = params[0], params[1]
                for _ in range(shiftnum):
                    rollover = displaymap[HEIGHT - 1][column]
                    for r in range(HEIGHT-1, 0, -1):
                        displaymap[r][column] = displaymap[r-1][column]
                    displaymap[0][column] = rollover

    finalsum = 0
    for row in displaymap:
        finalsum += sum(row)
    
    print(finalsum)

if __name__ == '__main__':
    main()

#Answer = 115