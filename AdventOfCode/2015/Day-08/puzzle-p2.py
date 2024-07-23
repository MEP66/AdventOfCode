import re

DAY = '08'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    total_string = 0
    total_coded = 0

    for line in input_data:
        total_string += len(line)
        num_quote = len(re.findall(r'"', line))
        num_slash = len(re.findall(r'\\', line))
        total_coded += (len(line) + num_quote + num_slash + 2)

    print(f'Answer: {total_coded} - {total_string} = {total_coded - total_string}')

    pass

if __name__ == '__main__':
    main()

#Answer = 2046