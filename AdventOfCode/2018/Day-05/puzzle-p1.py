

DAY = '05'
CASEDIFF = abs(ord('A')-ord('a'))

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = list(f.read().strip())

    i = 0
    end_of_str = len(input_data) - 1
    new_str = list()
    cur_char = input_data[i]

    while i < end_of_str:
        if abs(ord(cur_char)-ord(input_data[i+1])) == CASEDIFF:
            if new_str:
                i += 1
                cur_char = new_str.pop(-1)
            else:
                i += 2
                cur_char = input_data[i]
        else:
            new_str.append(cur_char)
            i += 1
            cur_char = input_data[i]
    if i == end_of_str:
        new_str.append(cur_char)

    print(f'Result: {len(new_str)}')


if __name__ == '__main__':
    main()

#Answer = 10762