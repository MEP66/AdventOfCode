from dataclasses import dataclass

DAY = '08'


@dataclass
class Hdr():
    c: int
    m: int


def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().split()]

    i = 0
    total = 0
    hdr_stack = list()

    hdr_stack.append(Hdr(input_data[i], input_data[i+1]))
    i += 2

    while hdr_stack:
        if hdr_stack[-1].c == 0:
            cur_hdr = hdr_stack.pop(-1)
            total += sum(input_data[i:i+cur_hdr.m])
            i += cur_hdr.m
        else:
            hdr_stack[-1].c -= 1
            hdr_stack.append(Hdr(input_data[i], input_data[i+1]))
            i += 2

    print(f'Sum total is: {total}')


if __name__ == '__main__':
    main()

#Answer = 40984