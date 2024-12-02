import re


DAY = '14'


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    memory = dict()
    for line in input_data:
        if line[0:3] == 'mas':
            mask = [c for c in line[7:]]
        else:
            mem_loc, val = [int(x) for x in re.findall(r'\d+', line)]
            val_bin = list(bin(val)[2:].zfill(36))
            for i, c in enumerate(mask):
                if c == '1':
                    val_bin[i] = '1'
                elif c == '0':
                    val_bin[i] = '0'
            memory[mem_loc] = int('0b' + ''.join(val_bin), 2)

    final_sum = sum(memory.values())
    print(f'Final sum: {final_sum}')


if __name__ == '__main__':
    main()

#Answer = 14954914379452