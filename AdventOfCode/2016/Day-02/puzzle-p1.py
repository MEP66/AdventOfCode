

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    location = [1, 1]
    for line in input_data:
        for char in line:
            match char:
                case 'L':
                    location[0] = max(0, location[0] - 1)
                case 'R':
                    location[0] = min(2, location[0] + 1)
                case 'D':
                    location[1] = min(2, location[1] + 1)
                case 'U':
                    location[1] = max(0, location[1] - 1)
        print(f'{location} => {(location[1] * 3) + (location[0] + 1)}')

if __name__ == '__main__':
    main()

#Answer = 44558