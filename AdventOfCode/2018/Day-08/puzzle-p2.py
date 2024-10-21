from dataclasses import dataclass

DAY = '08'


@dataclass
class Hdr():
    dc: int
    mc: int
    lp: int


@dataclass
class Node():
    nc: int
    cptr: list()
    md: list()
    nv: int


def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().split()]

    total = 0
    inp_ptr = 0
    hdr_stack = list()
    hdr_list = list()

    hdr_list.append(Node(nc=input_data[inp_ptr], cptr=list(), md=list(), nv=None))
    hdr_stack.append(Hdr(dc=input_data[inp_ptr], mc=input_data[inp_ptr+1], lp=len(hdr_list)-1))
    inp_ptr += 2

    while hdr_stack:
        if hdr_stack[-1].dc == 0:
            cur_hdr = hdr_stack.pop(-1)
            hdr_list[cur_hdr.lp].md = input_data[inp_ptr:inp_ptr+cur_hdr.mc]
            total += sum(hdr_list[cur_hdr.lp].md)
            if hdr_list[cur_hdr.lp].nc == 0:
                hdr_list[cur_hdr.lp].nv = sum(hdr_list[cur_hdr.lp].md)
            else:
                hdr_list[cur_hdr.lp].nv = sum([hdr_list[hdr_list[cur_hdr.lp].cptr[x-1]].nv
                                               for x in hdr_list[cur_hdr.lp].md
                                               if 0 < x <= hdr_list[cur_hdr.lp].nc])
            inp_ptr += cur_hdr.mc
        else:
            hdr_stack[-1].dc -= 1
            hdr_list.append(Node(nc=input_data[inp_ptr], cptr=list(), md=list(), nv=None))
            hdr_list[hdr_stack[-1].lp].cptr.append(len(hdr_list)-1)
            hdr_stack.append(Hdr(dc=input_data[inp_ptr], mc=input_data[inp_ptr+1], lp=len(hdr_list)-1))
            inp_ptr += 2

    print(f'Total metadata sum: {total}')
    print(f'Root node value: {hdr_list[0].nv}')


if __name__ == '__main__':
    main()

#Answer p1 = 40984
#Answer p2 = 37067