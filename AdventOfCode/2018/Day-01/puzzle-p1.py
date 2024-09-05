

DAY = '01'

def main():
    #filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    freq = 0
    for line in input_data:
        freq += int(line)

    print(f'Final frequency = {freq}')

if __name__ == '__main__':
    main()

#Answer = 402