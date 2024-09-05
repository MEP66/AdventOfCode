

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    horizontal = 0
    depth = 0
    for line in input_data:
        x = line.split()
        cmd = x[0]
        dist = int(x[1])
        match cmd:
            case 'up':
                depth -= dist
            case 'down':
                depth += dist
            case 'forward':
                horizontal += dist

    print(f'Horizontal = {horizontal}')
    print(f'depth = {depth}')
    print(f'prod = {horizontal * depth}')
if __name__ == '__main__':
    main()

#Answer = 1728414