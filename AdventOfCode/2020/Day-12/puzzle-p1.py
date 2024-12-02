

DAY = '12'

#Coordinates are in (x, y) or (c, r).
step = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
rotate90 = {'N': {'L': 'W', 'R': 'E'}, 'E': {'L': 'N', 'R': 'S'},
          'S': {'L': 'E', 'R': 'W'}, 'W': {'L': 'S', 'R': 'N'}}

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    nav_instr = list()
    for line in input_data:
        nav_instr.append((line[0], int(line[1:])))

    ship_loc = [0, 0]
    ship_facing = 'E'

    for instr, count in nav_instr:
        match instr:
            case 'L' | 'R':
                while count > 0:
                    ship_facing = rotate90[ship_facing][instr]
                    count -= 90
            case 'F':
                ship_loc[0] += (step[ship_facing][0] * count)
                ship_loc[1] += (step[ship_facing][1] * count)
            case 'N' | 'E' | 'S' | 'W':
                ship_loc[0] += (step[instr][0] * count)
                ship_loc[1] += (step[instr][1] * count)
            case _:
                print('Decoding error.')

    final_dist = abs(ship_loc[0]) + abs(ship_loc[1])
    print(f'Final distance: {final_dist}')

if __name__ == '__main__':
    main()

#Answer = 508