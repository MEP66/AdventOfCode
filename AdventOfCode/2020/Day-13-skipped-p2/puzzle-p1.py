

DAY = '13'


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    earliest_departure = int(input_data[0])
    buses = [int(x) for x in input_data[1].split(',') if x != 'x']

    time = earliest_departure
    found = False
    while not found:
        for n in buses:
            if not time % n:
                departure = time
                bus = n
                found = True
                break
        time += 1
    
    print(f'Result: {bus * (departure - earliest_departure)}')

if __name__ == '__main__':
    main()

#Answer = 2215