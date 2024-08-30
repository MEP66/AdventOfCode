

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()


    keypad = {(0, 2): ('1', {'L': (0, 0), 'R': (0, 0), 'U': (0, 0), 'D': (1, 0)}),
              (1, 1): ('2', {'L': (0, 0), 'R': (0, 1), 'U': (0, 0), 'D': (1, 0)}),
              (1, 2): ('3', {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}),
              (1, 3): ('4', {'L': (0, -1), 'R': (0, 0), 'U': (0, 0), 'D': (1, 0)}),
              (2, 0): ('5', {'L': (0, 0), 'R': (0, 1), 'U': (0, 0), 'D': (0, 0)}),
              (2, 1): ('6', {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}),
              (2, 2): ('7', {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}),
              (2, 3): ('8', {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}),
              (2, 4): ('9', {'L': (0, -1), 'R': (0, 0), 'U': (0, 0), 'D': (0, 0)}),
              (3, 1): ('A', {'L': (0, 0), 'R': (0, 1), 'U': (-1, 0), 'D': (0, 0)}),
              (3, 2): ('B', {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}),
              (3, 3): ('C', {'L': (0, -1), 'R': (0, 0), 'U': (-1, 0), 'D': (0, 0)}),
              (4, 2): ('D', {'L': (0, 0), 'R': (0, 0), 'U': (-1, 0), 'D': (0, 0)})
              }

    location = (2, 0)
    for line in input_data:
        for char in line:
            offset = keypad[location][1][char]
            location = (location[0] + offset[0], location[1] + offset[1])
        print(f'{location} => {keypad[location][0]}')

if __name__ == '__main__':
    main()

#Answer = 6BBAD