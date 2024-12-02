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
            ml_bin = list(bin(mem_loc)[2:].zfill(36))
            for i, c in enumerate(mask):
                if c == '1':
                    ml_bin[i] = '1'
            X_count = 0
            for c in mask:
                if c == 'X':
                    X_count += 1
            for xmask in range (2**X_count):
                xmask_i = 0
                for i, n in enumerate(mask):
                    if n == 'X':
                        ml_bin[i] = list(bin(xmask)[2:].zfill(X_count))[xmask_i]
                        xmask_i += 1
                memory[(int('0b' + ''.join(ml_bin), 2))] = val

    final_sum = sum(memory.values())
    print(f'Final sum: {final_sum}')
    

if __name__ == '__main__':
    main()

#Answer = 3415488160714