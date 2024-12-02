from math import lcm


DAY = '13'
START_TIME = 100000000000000

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    bus_departures = list()
    min_increment = 0
    for i, n in  enumerate(input_data[1].split(',')):
        if n != 'x':
            bus_departures.append([int(n), i])
            if int(n) > min_increment:
                min_increment = int(n)
                min_offset = -i
    
    start = START_TIME
    while start % min_increment:
        start += 1
    
    found = False
    while True:
        for b, ofs in bus_departures:
            if (start+ofs+min_offset) % b:
                break
        else:
            found = True
        if found:
            break
        start += min_increment

    
    print(f'Result: {start}')

if __name__ == '__main__':
    main()

#Answer = 1,549,033,645,149,029 is too high
#           149,669,104,223,100 is too low