import re

DAY = '05'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    matrix = []    
    for row, line in enumerate(input_data):
        if line:
            for col, c in enumerate(line):
                if c not in ['[', ']', ' ']:
                    matrix.append((c, row, col))
        else:
            movestart = row + 1
            break

    matrix2 = sorted(sorted(matrix, key = lambda x : x[1], reverse=True), key = lambda x : x[2])
    
    crates = dict()
    for element in matrix2:
        if element[0].isdigit():
            index = int(element[0])
            crates[index] = []
        else:
            crates[index].append(element[0])
    
    for line in input_data[movestart:]:
        datapts = re.findall(r'\d+', line)
        count, source, dest = map(int, datapts)

        crates[dest].extend(list(crates[source][-count:]))
        del crates[source][-count:]

    result = ''.join([stack[-1] for stack in crates.values()])

    print(f'The top if each stack result is: {result}')


if __name__ == '__main__':
    main()

# Answer = RGLVRCQSB
    