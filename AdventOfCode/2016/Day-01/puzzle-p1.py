from dataclasses import dataclass

DAY = '01'

@dataclass
class dir:
    turn: str
    dist: int

Heading = {'N': ({'R': 'E', 'L': 'W'}, (1, 0)), 'E': ({'R': 'S', 'L': 'N'}, (0, 1)),
            'S': ({'R': 'W', 'L': 'E'}, (-1, 0)), 'W': ({'R': 'N', 'L': 'S'}, (0, -1))}

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        directions = [dir(turn = x[0], dist = int(x[1:])) for x in f.read().strip().split(', ')]

    cur_location = (0, 0)
    cur_heading = 'N'

    for entry in directions:
        cur_heading = Heading[cur_heading][0][entry.turn]
        cur_location = (cur_location[0] + Heading[cur_heading][1][0] * entry.dist,
                        cur_location[1] + Heading[cur_heading][1][1] * entry.dist)
    
    print(f'{cur_location}, {abs(cur_location[0]) + abs(cur_location[1])}')

if __name__ == '__main__':
    main()

#Answer = 209