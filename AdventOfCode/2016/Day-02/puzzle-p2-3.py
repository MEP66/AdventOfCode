

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    keypad_p1 = {'1': {'R': '2', 'D': '4'},
                 '2': {'L': '1', 'R': '3', 'D': '5'},
                 '3': {'L': '2', 'D': '6'},
                 '4': {'R': '5', 'D': '7', 'U': '1'},
                 '5': {'R': '6', 'D': '9', 'L': '4', 'U': '2'},
                 '6': {'D': '9', 'L': '5', 'U': '3'},
                 '7': {'U': '4', 'R': '8'},
                 '8': {'L': '7', 'U': '5', 'R': '9'},
                 '9': {'L': '8', 'U': '6'}
            }
    start_loc_p1 = '5'

    keypad_p2 = {'1': {'D': '3'},
              '2': {'R': '3', 'D': '6'},
              '3': {'L': '2', 'R': '4', 'U': '1', 'D': '7'},
              '4': {'L': '3', 'D': '8'},
              '5': {'R': '6'},
              '6': {'L': '5', 'R': '7', 'U': '2', 'D': 'A'},
              '7': {'L': '6', 'R': '8', 'U': '3', 'D': 'B'},
              '8': {'L': '7', 'R': '9', 'U': '4', 'D': 'C'},
              '9': {'L': '8'},
              'A': {'R': 'B', 'U': '6'},
              'B': {'L': 'A', 'R': 'C', 'U': '7', 'D': 'D'},
              'C': {'L': 'B', 'U': '8'},
              'D': {'U': 'B'}
              }
    start_loc_p2 = '5'


    for part, input in enumerate(((keypad_p1, start_loc_p1), (keypad_p2, start_loc_p2))):
        keypad, number = input
        combo = list()
        for line in input_data:
            for dir in line:
                if dir in keypad[number]:
                    number = keypad[number][dir]
            combo.append(number)
        print(f'Part {part+1} combo is {''.join(combo)}')


if __name__ == '__main__':
    main()

#Answer p1 = 44559
#Answer p2 = 6BBAD