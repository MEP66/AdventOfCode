from collections import Counter

DAY = '06'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    result = list()
    cols = len(input_data[0])
    for col in range(cols):
        counts = Counter()
        for line in input_data:
            counts.update(line[col])
        result.append(max(counts, key=counts.get))

    print(''.join(result))

if __name__ == '__main__':
    main()

#Answer = bjosfbce