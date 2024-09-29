from collections import Counter


DAY = '02'

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    num_doubles, num_triples = 0, 0
    for line in input_data:
        char_count = Counter(line)
        counts = char_count.values()
        if 2 in counts:
            num_doubles += 1
        if 3 in counts:
            num_triples += 1
    
    print(f'Result: {num_doubles * num_triples}')


if __name__ == '__main__':
    main()

#Answer = 5000