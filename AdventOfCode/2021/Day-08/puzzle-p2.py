from collections import Counter

DAY = '08'

'''
Seg a appears in 8 numbers
Seg b appears in 6 numbers (unique)
Seg c appears in 8 numbers
Seg d appears in 7 numbers
Seg e appears in 4 numbers (unique)
Seg f appears in 9 numbers (unique)
Seg g appears in 7 numbers

Seg a appears in 7 and not in 1. That determines those two.
Seg d appears in 4, which is unique. Seg g is left over.

Num 1 has 2 segments (unique)
Num 2 has 5 segments
Num 3 has 5 segments
Num 4 has 4 segments (unique)
Num 5 has 5 segments
Num 6 has 6 segments
Num 7 has 3 segments (unique)
Num 8 has 7 segments (unique)
Num 9 has 5 segments
Num 0 has 6 segments
'''


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[x.split(' ') for x in line.split(' | ')] for line in f.read().splitlines()]

    code_to_digit = dict()
    code_to_digit['abcefg'] = '0'
    code_to_digit['cf'] = '1'
    code_to_digit['acdeg'] = '2'
    code_to_digit['acdfg'] = '3'
    code_to_digit['bcdf'] = '4'
    code_to_digit['abdfg'] = '5'
    code_to_digit['abdefg'] = '6'
    code_to_digit['acf'] = '7'
    code_to_digit['abcdefg'] = '8'
    code_to_digit['abcdfg'] = '9'

    output_total = 0

    for line in input_data:
        input = [''.join(sorted(list(x))) for x in line[0]]
        output = [''.join(sorted(list(x))) for x in line[1]]
        
        all_codes = set(input).union(set(output))
        if len(all_codes) != 10:
            print(f'Error: not all digits represented.')

        vcode_to_digit = dict()
        digit_to_vcode = dict()
        segcounts = Counter()
        for code in all_codes:
            segcounts.update(list(code))
            match len(code):
                case 2:
                    vcode_to_digit[code] = '1'
                    digit_to_vcode[1] = code
                case 3:
                    vcode_to_digit[code] = '7'
                    digit_to_vcode[7] = code
                case 4:
                    vcode_to_digit[code] = '4'
                    digit_to_vcode[4] = code
                case 7:
                    vcode_to_digit[code] = '8'
                    digit_to_vcode[8] = code
                case _:
                    pass
        
        seg_v_to_a = dict()
        for k, v in segcounts.items():
            match v:
                case 4:
                    seg_v_to_a[k] = 'e'
                case 6:
                    seg_v_to_a[k] = 'b'
                case 9:
                    seg_v_to_a[k] = 'f'
                case 7:
                    if k in digit_to_vcode[4]:
                        seg_v_to_a[k] = 'd'
                    else:
                        seg_v_to_a[k] = 'g'
                case 8:
                    if k not in digit_to_vcode[1]:
                        seg_v_to_a[k] = 'a'
                    else:
                        seg_v_to_a[k] = 'c'

        for vcode in all_codes:
            if len(vcode) in [5, 6]:
                code = ''.join(sorted([seg_v_to_a[vchar] for vchar in vcode]))
                vcode_to_digit[vcode] = code_to_digit[code]

        number = int(''.join([vcode_to_digit[vcode] for vcode in output]))
        output_total += number
        
    print(f'Total: {output_total}')


if __name__ == '__main__':
    main()

#Answer = 983026
