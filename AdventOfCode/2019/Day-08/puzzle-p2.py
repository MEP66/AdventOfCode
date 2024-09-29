from math import inf


DAY = '08'

def main():
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2019/Day-{DAY}/input.txt'
    
    WIDTH = 25
    HEIGHT = 6

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read()]

    rows = [input_data[r:r+WIDTH] for r in range(0, len(input_data), WIDTH)]
    images = [rows[c:c+HEIGHT] for c in range(0, len(rows), HEIGHT)]
    
    del rows, input_data
    
    final_image = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    for image in images:
        for r, row in enumerate(image):
            for c, char in enumerate(row):
                if final_image[r][c] == '.':
                    match char:
                        case 1:
                            final_image[r][c] = '*'
                        case 0:
                            final_image[r][c] = ' '
                        case _:
                            pass

    for row in final_image:
        print(f'{''.join(row)}')

if __name__ == '__main__':
    main()

#Answer = ZPZUB