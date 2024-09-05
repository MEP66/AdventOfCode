from operator import xor

DAY = '03'

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    input_data = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            input_data.append(tuple([int(bit) for bit in line.strip()]))

    transform = list(zip(*input_data))
    compbits = (len(transform[0]) / 2)
    bitcounts = [sum(x) for x in transform]
    numbits = len(bitcounts)
    result = int(''.join(['1' if count > compbits else '0' for count in bitcounts]), 2)

    print(f'Final product = {result * (xor(result, (2**numbits - 1)))}')

if __name__ == '__main__':
    main()

#Answer = 3882564