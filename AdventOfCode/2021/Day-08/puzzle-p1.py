

DAY = '08'

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[x.split(' ') for x in line.split(' | ')] for line in f.read().splitlines()]

    count = 0

    for line in input_data:
        for code in line[1]:
            if len(code) in (2, 3, 4, 7):
                count += 1
    
    print(f'Final count: {count}')
    pass

if __name__ == '__main__':
    main()

#Answer = 245
