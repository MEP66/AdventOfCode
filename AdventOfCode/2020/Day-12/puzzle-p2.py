

DAY = '12'

#Coordinates are in (x, y) or (c, r).
step = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1),  'W': (-1, 0)}
rotate90 = {'L': (-1, 1), 'R': (1, -1)}

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    nav_instr = list()
    for line in input_data:
        nav_instr.append((line[0], int(line[1:])))

    ship_loc = [0, 0]
    wp_relloc = [10,  1]

    for instr, count in nav_instr:
        match instr:
            case 'L' | 'R':
                while count > 0:
                    wp_relloc = [wp_relloc[1] * rotate90[instr][0], wp_relloc[0] * rotate90[instr][1]]
                    count -= 90
            case 'F':
                ship_loc[0] += (wp_relloc[0] * count)
                ship_loc[1] += (wp_relloc[1] * count)
            case 'N' | 'E' | 'S' | 'W':
                wp_relloc[0] += (step[instr][0] * count)
                wp_relloc[1] += (step[instr][1] * count)
            case _:
                print('Decoding error.')

    final_dist = abs(ship_loc[0]) + abs(ship_loc[1])
    print(f'Final distance: {final_dist}')

if __name__ == '__main__':
    main()

#Answer = 30761