

DAY = '08'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    total_string = 0
    total_memory = 0

    for line in input_data:
        total_string += len(line)
        total_memory += len(eval(line))

    print(f'Answer = {total_string - total_memory}')

    pass

if __name__ == '__main__':
    main()

#Answer = 1333