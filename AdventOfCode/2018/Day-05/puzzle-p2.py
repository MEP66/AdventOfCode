from math import inf


DAY = '05'
CASEDIFF = abs(ord('A')-ord('a'))

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().strip()


    reduced_min = inf
    for char_del in range(ord('a'), ord('z') + 1):
        reduced_str = list(input_data.replace(chr(char_del), '').replace(chr(char_del - CASEDIFF), ''))

        i = 0
        end_of_str = len(reduced_str) - 1
        new_str = list()
        cur_char = reduced_str[i]

        while i < end_of_str:
            if abs(ord(cur_char)-ord(reduced_str[i+1])) == CASEDIFF:
                if new_str:
                    i += 1
                    cur_char = new_str.pop(-1)
                else:
                    i += 2
                    cur_char = reduced_str[i]
            else:
                new_str.append(cur_char)
                i += 1
                cur_char = reduced_str[i]
        if i == end_of_str:
            new_str.append(cur_char)

        reduced_min = min(reduced_min, len(new_str))

    print(f'Result: {reduced_min}')


if __name__ == '__main__':
    main()

#Answer = 13263 is too high
#           10296 is too high