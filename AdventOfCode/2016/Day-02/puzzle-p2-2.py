

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    keypad_p1 = {(0, 0): ('1', ('R', 'D')),
                 (0, 1): ('2', ('L', 'R', 'D')),
                 (0, 2): ('3', ('L', 'D')),
                 (1, 0): ('4', ('R', 'D', 'U')),
                 (1, 1): ('5', ('R', 'D', 'L', 'U')),
                 (1, 2): ('6', ('D', 'L', 'U')),
                 (2, 0): ('7', ('U', 'R')),
                 (2, 1): ('8', ('L', 'U', 'R')),
                 (2, 2): ('9', ('L', 'U'))
            }
    start_loc_p1 = (1, 1)

    keypad_p2 = {(0, 2): ('1', ('D')),
              (1, 1): ('2', ('R', 'D')),
              (1, 2): ('3', ('L', 'R', 'U', 'D')),
              (1, 3): ('4', ('L', 'D')),
              (2, 0): ('5', ('R')),
              (2, 1): ('6', ('L', 'R', 'U', 'D')),
              (2, 2): ('7', ('L', 'R', 'U', 'D')),
              (2, 3): ('8', ('L', 'R', 'U', 'D')),
              (2, 4): ('9', ('L')),
              (3, 1): ('A', ('R', 'U')),
              (3, 2): ('B', ('L', 'R', 'U', 'D')),
              (3, 3): ('C', ('L', 'U')),
              (4, 2): ('D', ('U'))
              }
    start_loc_p2 = (2, 0)

    offset = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    for part, input in enumerate(((keypad_p1, start_loc_p1), (keypad_p2, start_loc_p2))):
        keypad, location = input
        combo = list()
        for line in input_data:
            for char in line:
                if char in keypad[location][1]:
                    location = (location[0] + offset[char][0], location[1] + offset[char][1])
            combo.append({keypad[location][0]})
        print(f'Part {part} combo is {combo}')


if __name__ == '__main__':
    main()

#Answer = 6BBAD